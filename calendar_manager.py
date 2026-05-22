import os
import datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.events']

def get_calendar_service():
    """Shows basic usage of the Google Calendar API.
    Authenticates the user and returns the calendar service object.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists('credentials.json'):
                raise FileNotFoundError("credentials.json not found! Please save it in this directory.")
            
            # Since this runs in github actions later, we will initially authenticate locally 
            # to generate the token.json, and then supply the token.json as a secret.
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)
        return service
    except HttpError as error:
        print(f'An error occurred building the calendar service: {error}')
        return None

def add_contest_event(service, contest):
    """
    Adds a single contest to Google Calendar with a 30-minute reminder.
    """
    if not service:
        print("Calendar service is not available.")
        return None

    # Contest start time is usually in 'YYYY-MM-DDTHH:MM:SS' UTC format from Clist
    # We parse it to a datetime object
    try:
        start_time = datetime.datetime.strptime(contest['start'], '%Y-%m-%dT%H:%M:%S')
        end_time = datetime.datetime.strptime(contest['end'], '%Y-%m-%dT%H:%M:%S')
    except ValueError as e:
        print(f"Error parsing time for contest {contest.get('event')}: {e}")
        return None

    event_body = {
        'summary': f"{contest['event']} ({contest['resource']})",
        'location': contest['href'],
        'description': f"Competitive Programming Contest on {contest['resource']}.\nLink: {contest['href']}",
        'start': {
            'dateTime': start_time.isoformat() + 'Z',
            'timeZone': 'UTC',
        },
        'end': {
            'dateTime': end_time.isoformat() + 'Z',
            'timeZone': 'UTC',
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
                # This explicitly sets a 30-minute pop-up reminder
                {'method': 'popup', 'minutes': 30},
            ],
        },
    }

    try:
        # Check if event already exists (we search by event name within a small timeframe)
        time_min = (start_time - datetime.timedelta(hours=1)).isoformat() + 'Z'
        time_max = (start_time + datetime.timedelta(hours=1)).isoformat() + 'Z'
        
        events_result = service.events().list(
            calendarId='primary', timeMin=time_min, timeMax=time_max,
            singleEvents=True, orderBy='startTime').execute()
        events = events_result.get('items', [])

        for existing_event in events:
            if existing_event.get('summary') == event_body['summary']:
                print(f"Skipping... Event already exists: {existing_event['summary']}")
                return existing_event

        print(f"Creating new event: {event_body['summary']}")
        event = service.events().insert(calendarId='primary', body=event_body).execute()
        print(f"Event created successfully: {event.get('htmlLink')}")
        return event

    except HttpError as error:
        print(f'An error occurred adding the event: {error}')
        raise error

if __name__ == '__main__':
    # Simple test logic
    service = get_calendar_service()
    if service:
        print("Successfully authenticated with Google Calendar!")

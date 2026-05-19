import time
from clist_fetcher import fetch_upcoming_contests
from calendar_manager import get_calendar_service, add_contest_event

def main():
    print("Starting Contest Reminder Agent...")
    
    # 1. Authenticate with Google Calendar
    print("Authenticating with Google Calendar...")
    service = get_calendar_service()
    if not service:
        print("Failed to authenticate with Google Calendar. Exiting.")
        return

    # 2. Fetch upcoming contests
    print("Fetching upcoming contests from Clist API...")
    contests = fetch_upcoming_contests(days_ahead=14)
    
    if not contests:
        print("No upcoming contests found for the selected platforms.")
        return
        
    print(f"Found {len(contests)} contests. Syncing with Google Calendar...")

    # 3. Add to Calendar
    for contest in contests:
        # Sleep briefly to avoid hitting Google Calendar API rate limits
        time.sleep(1)
        
        add_contest_event(service, contest)

    print("Finished processing contests. All set!")

if __name__ == "__main__":
    main()

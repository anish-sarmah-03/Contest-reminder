import os
import requests
from datetime import datetime, timedelta, timezone

# Clist API Credentials — loaded from environment variables (never hardcode!)
USERNAME = os.environ.get('CLIST_USERNAME')
API_KEY  = os.environ.get('CLIST_API_KEY')

if not USERNAME or not API_KEY:
    raise EnvironmentError(
        "Missing Clist API credentials! "
        "Set CLIST_USERNAME and CLIST_API_KEY environment variables."
    )

# Target resources (platforms)
TARGET_RESOURCES = [
    'codeforces.com',
    'codechef.com',
    'leetcode.com'
]

def fetch_upcoming_contests(days_ahead=14):
    """
    Fetches upcoming contests from Clist API for specified platforms.
    """
    base_url = "https://clist.by/api/v4/contest/"
    
    # Time filtering: From now to `days_ahead` in the future
    now = datetime.now(timezone.utc)
    future = now + timedelta(days=days_ahead)
    
    start_time_gte = now.strftime('%Y-%m-%dT%H:%M:%S')
    start_time_lte = future.strftime('%Y-%m-%dT%H:%M:%S')
    
    headers = {
        'Authorization': f'ApiKey {USERNAME}:{API_KEY}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    params = {
        'resource__in': ','.join(TARGET_RESOURCES),
        'start__gte': start_time_gte,
        'start__lte': start_time_lte,
        'order_by': 'start',
        'limit': 100 # Fetch up to 100 contests at a time
    }
    
    print(f"Fetching upcoming contests from {start_time_gte} to {start_time_lte}...")
    
    try:
        response = requests.get(base_url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        contests = data.get('objects', [])
        
        # Additional filtering in code to ensure only exact matching resources
        filtered_contests = [c for c in contests if c['resource'] in TARGET_RESOURCES]
        
        print(f"Fetched {len(filtered_contests)} upcoming target contests.")
        return filtered_contests
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Clist API: {e}")
        raise e

if __name__ == "__main__":
    contests = fetch_upcoming_contests()
    for contest in contests:
        print(f"{contest['event']} ({contest['resource']})")
        print(f"Start: {contest['start']}")
        print(f"Link: {contest['href']}")
        print("-" * 40)

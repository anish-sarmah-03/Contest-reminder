import requests
from datetime import datetime, timedelta, timezone

# Clist API Credentials
USERNAME = 'anish_sarmah'
API_KEY = 'a96dd18ec88fd26a6a0d277ac06ac209c344a8f2'

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
        'Authorization': f'ApiKey {USERNAME}:{API_KEY}'
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
        return []

if __name__ == "__main__":
    contests = fetch_upcoming_contests()
    for contest in contests:
        print(f"{contest['event']} ({contest['resource']})")
        print(f"Start: {contest['start']}")
        print(f"Link: {contest['href']}")
        print("-" * 40)

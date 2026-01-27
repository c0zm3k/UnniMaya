import urllib.request
import json

API_KEY = 'futurefit-dev-key-789'
BASE_URL = 'http://127.0.0.1:3000/api'
HEADERS = {'x-api-key': API_KEY}

def test_filter(endpoint, params):
    query_string = urllib.parse.urlencode(params)
    url = f"{BASE_URL}/{endpoint}?{query_string}"
    print(f"Testing {url}...")
    try:
        req = urllib.request.Request(url, headers=HEADERS)
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode())
            print(f"Results found: {len(data)}")
            if len(data) > 0:
                print(f"Sample: {data[0]}")
            return data
    except Exception as e:
        print(f"Error: {e}")
        return None

if __name__ == '__main__':
    # Test Course Filter
    test_filter('courses', {'stream': 'Engineering', 'level': 'UG'})
    
    # Test College Filter
    test_filter('colleges', {'type': 'Government', 'location': 'Bangalore'})
    
    # Test Job Filter
    test_filter('jobs', {'experience': 'Fresher', 'mode': 'WFH'})
    
    # Test Reset (No params)
    res = test_filter('courses', {})
    if res is not None and len(res) == 5:
        print("Reset/Default check PASSED: Result count is exactly 5.")
    else:
        print(f"Reset/Default check FAILED: Expected 5, got {len(res) if res else 'None'}.")

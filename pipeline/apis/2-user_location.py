#!/usr/bin/env python3
import sys
import requests
import time

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <GitHub API URL>".format(sys.argv[0]))
        sys.exit(1)
    
    url = sys.argv[1]
    try:
        response = requests.get(url)
    except Exception as e:
        print("Error:", e)
        sys.exit(1)
    
    if response.status_code == 403:
        # The API returns status 403 when the rate limit is exceeded.
        # The header "X-RateLimit-Reset" contains the epoch time when the limit resets.
        reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
        current_time = int(time.time())
        minutes = (reset_time - current_time) // 60
        print("Reset in {} min".format(minutes))
    elif response.status_code == 404:
        # The user does not exist.
        print("Not found")
    elif response.status_code == 200:
        data = response.json()
        # Print the user's location if available, otherwise "Not found"
        location = data.get('location')
        if location:
            print(location)
        else:
            print("Not found")
    else:
        print("Not found")

if __name__ == '__main__':
    main()


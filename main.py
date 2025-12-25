from sys import argv
from http.client import HTTPResponse
from urllib.request import *
import json;

# https://api.github.com/users/<username>/events
# Example: https://api.github.com/users/kamranahmedse/events



def main():
    if len(argv)!= 2:
        raise Exception("ERROR: Improper usage, Example: python3 gh-activity.py <username>")
    
    user = argv[-1]
    url = f"https://api.github.com/users/{user}/events"
    
    try:
        with urlopen(url) as api:
            if not isinstance(api, HTTPResponse):
                raise Exception(f"ERROR: HTTP RESPONSE NOT RETURNED")
            
            if api.status != 200:
                raise Exception(f"ERROR: {api.status}")
            
            header = api.headers
            data = api.read()
            if "application/json" not in api.headers["Content-Type"]:
                decoded_json = json.loads(data)
                print(decoded_json)
    except Exception as e:
        print(e)

    
    
if __name__ == "__main__":
    main()

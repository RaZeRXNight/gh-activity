from sys import argv
from urllib.request import *

# https://api.github.com/users/<username>/events
# Example: https://api.github.com/users/kamranahmedse/events



def main():
    if len(argv)!= 2:
        raise Exception("ERROR: Improper usage, Example: python3 gh-activity.py <username>")
    
    user = argv[-1]
    url = f"https://api.github.com/users/{user}"
    

    api_request = urlopen(url, None, 5.0)
    
    if api_request.status != 200:
        raise Exception(f"ERROR: {api_request.status}")
    
    
    
if __name__ == "__main__":
    main()

from sys import argv
from http.client import HTTPResponse
from urllib.request import urlopen
import json;

# https://api.github.com/users/<username>/events
# Example: https://api.github.com/users/kamranahmedse/events



def main():
    user = argv[-1]
    url = f"https://api.github.com/users/{user}/events/public"

    try:
        with urlopen(url) as api:
            if not isinstance(api, HTTPResponse):
                raise Exception(f"ERROR: HTTP RESPONSE NOT RETURNED")
            
            if api.status != 200:
                raise Exception(f"ERROR: {api.status}")
            
            if "application/json" in api.headers["Content-Type"]:
                decoded_json = json.loads(api.read())
                if not decoded_json:
                    print(f"{user} has no recent user activities")
                    return
                
                # Cycle through each event returned by the api
                for i in decoded_json:
                    event = i["type"]
                    payload = i["payload"]

                    match(event):
                        case "CreateEvent":
                            print("-", f"Created {payload["ref_type"]} in {i["repo"]["name"]} {payload["ref"]}")
                        case "DeleteEvent":
                            print("-", f"{payload["pusher_type"]} Deleted {payload["ref_type"]} on {i["repo"]["name"]}")
                        case "DiscussionEvent":
                            print("-", f"Started a Discussion {payload["discussion"]}")
                        case "ForkEvent":
                            print("-", f"{payload["action"]} {payload["forkee"]} of {i["repo"]["name"]}")
                        case "CommitCommentEvent":
                            print("-", f"Commit Commented {payload["action"]} on {i["repo"]["name"]}")
                        case "PushEvent":
                            print("-", f" to {i["repo"]["name"]}")
                        case "PullRequestEvent":
                            print("-", f"{payload["action"]} Pull Request {payload["pull_request"]} on {i["repo"]["name"]}")
                        case "PullRequestReviewEvent":
                            print("-", f"{payload["action"]} Pull Request {payload["pull_request"]["number"]} on {i["repo"]["name"]}")
                        case "PushEvent":
                            print("-", f"Pushed on {payload["ref"]}")
                        case "WatchEvent":
                            print("-", f"{payload["action"]} watching {i["repo"]["name"]}")
                        case _:
                            print()
            else:
                print(f"ERROR: unable to fetch {user}'s events in a proper format (json)")
                api.close()
    except Exception as e:
        print(e)

    
    
if __name__ == "__main__":
    if len(argv)!= 2:
        raise Exception("ERROR: Improper usage, Example: python3 gh-activity.py <username>")
    
    main()

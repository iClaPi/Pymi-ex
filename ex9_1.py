import requests
import sys

def get_user_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    repositories = response.json()

    return repositories

def list_user_repositories(username):
    repositories = get_user_repositories(username)

    if isinstance(repositories, list):
        for repo in repositories:
            print(repo["name"])
    else:
        print(f"Error: {repositories['message']}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 githubrepos.py username")
        sys.exit(1)

    username = sys.argv[1]
    list_user_repositories(username)

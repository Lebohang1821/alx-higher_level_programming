#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""
import requests
import sys

def fetch_commits(repository, owner):
    base_url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = requests.get(base_url)
    commits = response.json()

    for commit in commits[:10]:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script_name.py <repository_name> <owner_name>")
        sys.exit(1)

    repository_name = sys.argv[1]
    owner_name = sys.argv[2]

    fetch_commits(repository_name, owner_name)

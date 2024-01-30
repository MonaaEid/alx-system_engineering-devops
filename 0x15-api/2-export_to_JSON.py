#!/usr/bin/python3
"""comment"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    username = user.get("username")
    todo = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    with open("{}.json".format(user), "w") as jsonfile:
        json.dump({user: [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": username
            } for t in todo]}, jsonfile)
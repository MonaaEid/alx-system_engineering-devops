#!/usr/bin/python3
"""comment"""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed_tasks = [{"task": t.get("title"), "completed": t.get(
        "completed"), "username": user.get("name")} for t in todos]
    data = {sys.argv[1]: completed_tasks}
    filename = "{}.json".format(sys.argv[1])
    with open(filename, "w") as f:
        json.dump(data, f)

    print("Data exported to file: {}".format(filename))

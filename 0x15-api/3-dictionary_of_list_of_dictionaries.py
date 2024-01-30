#!/usr/bin/python3
"""task three"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    data = {}
    for user in users:
        todos = requests.get(url + "todos", params={"userId": user.get("id")}).json()
        completed_tasks = [{"task": t.get("title"), "completed": t.get("completed"), "username": user.get("name")} for t in todos]
        data[user.get("id")] = completed_tasks

    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(data, f)
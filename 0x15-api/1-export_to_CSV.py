#!/usr/bin/python3
""" Python script to export data in the CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed_tasks = [
        (sys.argv[1],
         user.get("name"),
         t.get("completed"),
         t.get("title")) for t in todos]
    filename = "{}.csv".format(sys.argv[1])
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        writer.writerows(completed_tasks)

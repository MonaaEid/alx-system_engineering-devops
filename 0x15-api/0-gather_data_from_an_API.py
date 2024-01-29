#!/usr/bin/python3
"""using this REST API, for a given employee ID, returns
information about his/her todo list progress."""
import json
import sys
import urllib.request


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}".format(sys.argv[1])

    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        employee_name = data["name"]

    url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
        sys.argv[1])
    with urllib.request.urlopen(url) as response:
        data = json.loads(response.read().decode())
        total_number_of_tasks = len(data)
        number_of_done_tasks = sum([1 for task in data if task["completed"]])

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          number_of_done_tasks, total_number_of_tasks))
    for task in data:
        if task["completed"]:
            print("\t{} {}".format("\t", task["title"]))
    # fhand = urllib.request.urlopen(url)
    # for line in fhand:
    #     print(line.decode().strip())
    # print(fhand)

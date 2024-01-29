import csv
import json
import sys
import urllib.request

if len(sys.argv) != 2:
    print("Usage: {} EMPLOYEE_ID".format(sys.argv[0]))
    sys.exit(1)

employee_id = sys.argv[1]

url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())
    employee_name = data["name"]

url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(
    employee_id)
with urllib.request.urlopen(url) as response:
    data = json.loads(response.read().decode())

filename = "{}.csv".format(employee_id)
with open(filename, mode='w', newline='') as csv_file:
    fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    writer.writeheader()
    for task in data:
        writer.writerow(
            {
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': 'completed' if task["completed"] else 'not completed',
                'TASK_TITLE': task["title"]})
print("Data written to file: {}".format(filename))

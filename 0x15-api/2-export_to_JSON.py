#!/usr/bin/python3
"""comment"""
import csv
import json
import sys


if __name__ == "__main__":
    data = []
    with open('tasks.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['USER_ID'] == sys.argv[1]:
                data.append({
                    'task': row['TASK_TITLE'],
                    'completed': row['TASK_COMPLETED_STATUS'] == 'True',
                    'username': row['USERNAME']
                })

    json_string = json.dumps({sys.argv[1]: data})

    with open(f'{sys.argv[1]}.json', 'w') as file:
        file.write(json_string)
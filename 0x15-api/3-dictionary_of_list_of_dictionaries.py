#!/usr/bin/python3
"""task three"""
import csv
import json


if __name__ == "__main__":
    # Step 1: Initialize a Python Dictionary
    data = {}

    # Step 2: Read the lines of CSV file using csv.DictReader() function
    with open('tasks.csv') as file:
        reader = csv.DictReader(file)

        # Step 3: Convert each line into a dictionary
        for row in reader:
            user_id = row['USER_ID']
            task = {
                'username': row['USERNAME'],
                'task': row['TASK_TITLE'],
                'completed': row['TASK_COMPLETED_STATUS'] == 'True'
            }

            # Step 4: Add the dictionary to the Python Dictionary created in step 1
            if user_id in data:
                data[user_id].append(task)
            else:
                data[user_id] = [task]

    # Step 5: Convert the Python Dictionary to JSON String using json.dumps()
    json_string = json.dumps(data)

    # Step 6: You may write the JSON String to a JSON file
    with open('todo_all_employees.json', 'w') as file:
        file.write(json_string)

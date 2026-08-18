"""Python Projects #2: Task Tracker CLI
Allows users to add, change the status of, edit, and delete tasks from a to-do list
The list is saved as a JSON"""
"""
import json
import argparse

parser = argparse.ArgumentParser(
    description = "Allows task input."
)

parser.add_argument(
    "-n","--name", metavar="name",
    required = True, help= "The name of the person to greet."
)

args = parser.parse_args()

msg = f"Hello {args.name}!"
print(msg)

json_task_string = '''
    {
        "tasks": [
            {
                "id": 1,
                "description": "walk dogs",
                "status": "todo",
                "createdAt": "8/18/26 1:16 P.M.",
                "updatedAt": "8/18/26 1:17 P.M."
            },
            {
                "id": 2,
                "description": "shower",
                "status": "todo",
                "createdAt": "8/18/26 1:18 P.M.",
                "updatedAt": "8/18/26 1:19 P.M."
            }
        ]
    }
'''

list = json.loads(json_task_string)
print(list['tasks'][0]['id'])

with open("tasks.json" , "w") as f:
    json.dump(list, f)
"""

import json
import argparse

#create dictionary for tasks
tasks_dict = {"tasks":[{}]} 

parser = argparse.ArgumentParser(
    description = "Allows task input."
)

parser.add_argument(
    "-a","--add", metavar="add",
    required = False, help= "Adding a new task"
)

args = parser.parse_args()

msg = f"Adding {args.add}."
tasks_dict["tasks"][0]["description"] = args.add
with open("tasks.json","w") as f:
    json.dump(tasks_dict, f)
print(msg)
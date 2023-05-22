#!/usr/bin/python3
""" Python script that export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    Id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(url, Id)
    user_info = requests.get(user_url).json()
    username = user_info.get("username")

    tasks_url = "{}/todos".format(url)
    tasks = requests.get(tasks_url).json()
    user_tasks = [obj for obj in tasks if obj.get("userId") == Id]

    output = {
        Id: [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            }
            for task in user_tasks
        ]
    }

    filename = "{}.json".format(Id)
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(output, file)

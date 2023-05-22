#!/usr/bin/python3
""" Python script that export data in the JSON format"""
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"

    users_url = "{}/users".format(url)
    users = requests.get(users_url).json()

    tasks_url = "{}/todos".format(url)
    tasks = requests.get(tasks_url).json()

    output = {
        user.get("id"): [
            {
                "username": user.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            for task in tasks
            if task.get("userId") == user.get("id")
        ]
        for user in users
    }

    filename = "todo_all_employees.json"
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(output, file)

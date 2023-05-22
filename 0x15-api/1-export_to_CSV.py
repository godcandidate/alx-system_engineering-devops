#!/usr/bin/python3
"""Python script that export data in the CSV format"""
import requests
import sys
import csv


if __name__ == "__main__":
    Id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(url, Id)
    user_info = requests.get(user_url).json()
    username = user_info.get("username")

    tasks_url = "{}/todos".format(url)
    tasks = requests.get(tasks_url).json()
    user_tasks = [obj for obj in tasks if obj.get("userId") == Id]

    output = [
        [
            str(Id),
            str(username),
            str(task.get("completed")),
            str(task.get("title"))
        ]
        for task in user_tasks
    ]

    filename = "{}.csv".format(Id)
    with open(filename, 'w', encoding="utf-8") as file:
        obj = csv.writer(file, quoting=csv.QUOTE_ALL)

        for row in output:
            obj.writerow(row)

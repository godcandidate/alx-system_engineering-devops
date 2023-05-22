#!/usr/bin/python3
# a Python script that, using this REST API, for a given employee ID
import requests
import sys


if __name__ == "__main__":
    Id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"

    user_url = "{}/users/{}".format(url, Id)
    user_info = requests.get(user_url).json()
    name = user_info.get("name")

    tasks_url = "{}/todos".format(url)
    tasks = requests.get(tasks_url).json()
    user_t = [obj for obj in tasks if obj.get("userId") == Id]
    tasks_d = [obj for obj in user_t if obj.get("completed")]
    us_t = len(user_t)
    t_done = len(tasks_d)

    print("Employee {} is done with tasks({}/{}):".format(name, t_done, us_t))
    for task in tasks_d:
        print("\t {}".format(task.get("title")))

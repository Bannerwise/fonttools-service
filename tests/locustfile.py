from locust import HttpLocust, TaskSet
import json

with open('example.json') as json_data:
    font = json.load(json_data)

def subset(l):
    l.client.post("/subset", headers={'content-type': 'application/json'}, data=json.dumps(font))

class UserBehavior(TaskSet):
    tasks = { subset: 5 }

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000

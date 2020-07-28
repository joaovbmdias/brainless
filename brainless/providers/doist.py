import uuid
import requests
import json
import datetime
import constants as const

def get_projects(api_token):
    data = []

    projects = requests.get("https://api.todoist.com/rest/v1/projects", headers={"Authorization": "Bearer %s" % api_token}).json()

    for pr in projects:
        data.append({'name': pr['name'], 'guid': pr['id'], 'tasks': []})

    return data

def get_tasks(api_token, projects):

    for pr in projects:
        tasks = requests.get("https://api.todoist.com/rest/v1/tasks", params={"project_id": pr['guid']}, headers={"Authorization": "Bearer %s" % api_token}).json()

        for ts in tasks:
            try:
                due = ts.pop('due',None)
                due_datetime = None
                if due is not None:
                    due = due.pop('datetime',due.pop('date',None))
                    due_datetime = datetime.datetime.strptime(due, '%Y-%m-%d %H:%M:%S.%f')
            except:
                pass

            task = {'name': ts['content'], 'guid': ts['id'], 'priority': ts['priority'], 'labels': ts['label_ids'], 'due_datetime': due_datetime}

            pr['tasks'].append(task)

    return projects

def schedule_task(api_token):
    requests.post( "https://api.todoist.com/rest/v1/tasks/1234", data=json.dumps({"content": "Movies to watch"}),headers={"Content-Type": "application/json", "X-Request-Id": str(uuid.uuid4()), "Authorization": "Bearer %s" % api_token})

def get_labels(api_token):
    data = []

    labels = requests.get("https://api.todoist.com/rest/v1/labels", headers={"Authorization": "Bearer %s" % api_token}).json()

    for lb in  labels:
        data.append({'name': lb['name'], 'guid': lb['id'], 'order': lb['order']})
    
    return data


def get_data(api_token):
    doist_data = {const.CALENDAR: None, const.TASK: None, const.LABEL: None}

    projects = get_projects(api_token)

    tasks = get_tasks(api_token, projects)

    labels = get_labels(api_token)

    doist_data[const.TASK] = tasks
    doist_data[const.LABEL] = labels

    return doist_data

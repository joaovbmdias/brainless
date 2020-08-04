"""
This is the task module and supports all the ReST actions for PROJECTS
"""

from flask import abort
from configuration import db
from models.task import Task, TaskSchema
from constants import FAILURE

def create(user_id, account_id, project_id, body):
    """
    This function creates a new task for a specific account,
    user and project combination based on the passed-in task data

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :param body: task to create in tasks structure
    :return: 201 on success, 409 on task already exists
    """
    schema = TaskSchema()
    task = schema.load(body)
    if task.create() == FAILURE:
        abort(409, f'Task {task.name} already exists')
    else:
        return schema.dump(task), 201

def read(user_id, account_id, project_id, task_id):
    """
    This function retrieves a task based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :param task_id: task_id passed-in URL
    :return: 200 on success, 404 on task already exists
    """
    task = Task(id           = task_id,
                name         = None,
                project_id   = None,
                due_datetime = None,
                priority     = None,
                guid         = None)
    if task.read() == FAILURE:
        abort(404, f'Task with id:{task_id} not found')
    else:
        schema = TaskSchema()
        return schema.dump(task), 200

def search(user_id, account_id, project_id):
    """
    This function retrieves a list of tasks based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :return: 200 on success, 404 on no tasks found
    """
    tasks = Task.query.filter(Task.project_id == project_id).all()
    if tasks is None:
        abort(404, f'No tasks found')
    schema = TaskSchema(many=True)
    return schema.dump(tasks), 200

def update(user_id, account_id, project_id, task_id, body):
    """
    This function updates an account based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :param task_id: task_id passed-in URL
    :param body: payload information
    :return: 200 on success, 404 on task not found
    """
    schema = TaskSchema()
    task = schema.load(body)
    if task.update() == FAILURE:
        abort(404, f'Task {task_id} not found')
    else:
        return schema.dump(task), 200

def delete(user_id, account_id, project_id, task_id):
    """
    This function deletes an task based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :param task_id: task_id passed-in URL
    :return: 200 on success, 404 on task not found
    """
    task = Task(id           = task_id,
                name         = None,
                project_id   = None,
                due_datetime = None,
                priority     = None,
                guid         = None)
    if task.delete() == FAILURE:
        abort(404, f'Task {task_id} not found')
    else:
        return "Task deleted", 200

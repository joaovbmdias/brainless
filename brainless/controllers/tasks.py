"""
This is the task module and supports all the ReST actions for PROJECTS
"""

from flask import abort
from configuration import db
from models.task import Task, TaskSchema
from sqlalchemy.orm.exc import NoResultFound

def create(user_id, account_id, project_id, task):
    """
    This function creates a new task for a specific account,
    user and project combination based on the passed-in task data

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :param task: task to create in tasks structure
    :return: 201 on success, 409 on task already exists
    """

    schema = TaskSchema()
    new_task = schema.load(task)

    if new_task.create() is None:
        abort(409, f'Task {new_task.name} already exists')
    else:
        task_serialized = schema.dump(new_task)

        return task_serialized, 201

def read(user_id, account_id, project_id, task_id):
    """
    This function retrieves a task based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :param task_id: task_id passed-in URL
    :return: 200 on success, 404 on task already exists
    """

    task = Task(task_id=task_id)

    read_task = task.read()

    if read_task is None:
        abort(404, f'Task with id:{task_id} not found')
    else:
        schema = TaskSchema()
        task_serialized = schema.dump(read_task)

        return task_serialized, 200

def search(user_id, account_id, project_id):
    """
    This function retrieves a list of tasks based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :return: 200 on success, 404 on no tasks found
    """

    existing_tasks = Task.query.filter(Task.project_id == project_id).all()
    if existing_tasks is None:
        abort(404, f'No tasks found')

    schema = TaskSchema(many=True)
    tasks = schema.dump(existing_tasks)

    return tasks, 200

def update(user_id, account_id, project_id, task_id, task):
    """
    This function updates an account based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :param task_id: task_id passed-in URL
    :param task: payload information
    :return: 200 on success, 404 on task not found
    """

    schema = TaskSchema()
    task_to_update = schema.load(task)

    updated_task = task_to_update.update()

    if updated_task is None:
        abort(404, f'Task {task_id} not found')
    else:
        task_serialized = schema.dump(updated_task)

        return task_serialized, 200

def delete(user_id, account_id, project_id, task_id):
    """
    This function deletes an task based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :param task_id: task_id passed-in URL
    :return: 200 on success, 404 on task not found
    """

    task_to_delete = Task(task_id=task_id)

    if task_to_delete.delete() is not None:
        abort(404, f'Task {task_id} not found')
    else:
        return "Task deleted", 200

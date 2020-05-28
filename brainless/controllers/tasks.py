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

    # get provided task guid
    guid = task.get('guid')

    # validate if an task with the provided data exists
    existing_task = (Task.query.filter(Task.guid == guid)
                                  .filter(Task.project_id == project_id)
                                  .one_or_none())

    if existing_task is None:
        schema = TaskSchema()

        # Create a task instance using the schema and the passed-in task
        new_task = schema.load(task)

        # Add the task to the database
        db.session.add(new_task)

        db.session.commit()

        # return the newly created task id in the response
        return new_task.task_id , 201

    else:
        abort(409, f'Task {guid} already exists for project {project_id}')

def read(user_id, account_id, project_id, task_id):
    """
    This function retrieves a task based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :param task_id: task_id passed-in URL
    :return: 200 on success, 404 on task already exists
    """

    try:
        # get task if it exists
        existing_task = Task.query.filter(Task.task_id == task_id).one()
    except NoResultFound:
        abort(404, f'Task with id:{task_id} not found')

    schema = TaskSchema()
    task = schema.dump(existing_task)

    return task, 200

def search(user_id, account_id, project_id):
    """
    This function retrieves a list of tasks based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :return: 200 on success, 404 on no tasks found
    """

    # search tasks for the user and acount ids provided
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

    try:
        # validate if task exists
        existing_task = Task.query.filter(Task.task_id == task_id).one()    
    except NoResultFound:
        abort(404, f'Task {task_id} not found')
    
    schema = TaskSchema()

    # Create an task instance using the schema and the passed-in task
    updated_task = schema.load(task)

    # Set the id to the task we want to update
    updated_task.task_id = existing_task.task_id

    # Add the task to the database
    db.session.merge(updated_task)
    db.session.commit()

    return "Task updated", 200

def delete(user_id, account_id, project_id, task_id):
    """
    This function deletes an task based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :param task_id: task_id passed-in URL
    :return: 200 on success, 404 on task not found
    """

    try:
        # validate if task exists
        existing_task = Task.query.filter(Task.task_id == task_id).one()
    except NoResultFound:
        abort(404, f'Task {task_id} not found')

    # Add the task to the database
    db.session.delete(existing_task)
    db.session.commit()

    return "Task deleted", 200

"""
This is the project module and supports all the ReST actions for PROJECTS
"""
from flask import abort
from configuration import db
from models.project import Project, ProjectSchema
from constants import FAILURE

def create(user_id, account_id, body):
    """
    This function creates a new project for a specific account
    of a specific user based on the passed-in project data

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param body: project to create in projects structure
    :return: 201 on success, 409 on project already exists
    """
    schema = ProjectSchema()
    project = schema.load(body)
    if project.create() == FAILURE:
        abort(409, f'Project {project.name} already exists')
    else:
        return schema.dump(project), 201

def read(user_id, account_id, project_id):
    """
    This function retrieves a project based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :return: 200 on success, 404 on project already exists
    """

    project = Project(id            = project_id,
                      name          = None,
                      guid          = None,
                      account_id    = None,
                      brain_enabled = None)
    if project.read() == FAILURE:
        abort(404, f'Project with id:{project_id} not found')
    else:
        schema = ProjectSchema()
        return schema.dump(project), 200

def search(user_id, account_id):
    """
    This function retrieves a list of projects based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :return: 200 on success, 404 on no projects found
    """
    projects = Project.query.filter(Project.account_id == account_id).all()
    if projects is None:
        abort(404, f'No projects found')
    schema = ProjectSchema(many=True)
    return schema.dump(projects), 200

def update(user_id, account_id, project_id, body):
    """
    This function updates an account based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :param project: payload information
    :return: 200 on success, 404 on project not found
    """
    schema = ProjectSchema()
    project = schema.load(body)

    if project.update() == FAILURE:
        abort(404, f'Project {project_id} not found')
    else:
        return schema.dump(project), 200

def delete(user_id, account_id, project_id):
    """
    This function deletes an project based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :return: 200 on success, 404 on project not found
    """
    project = Project(id            = project_id,
                      name          = None,
                      guid          = None,
                      account_id    = None,
                      brain_enabled = None)
    if project.delete() == FAILURE:
        abort(404, f'Project {project_id} not found')
    else:
        return "Project deleted", 200

"""
This is the project module and supports all the ReST actions for PROJECTS
"""

from flask import abort
from configuration import db
from models.project import Project, ProjectSchema

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

    if project.create() is None:
        abort(409, f'Project {project.name} already exists')
    else:
        project_serialized = schema.dump(project)

        return project_serialized, 201

def read(user_id, account_id, project_id):
    """
    This function retrieves a project based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :return: 200 on success, 404 on project already exists
    """

    project = Project(id=project_id,
                      name=None,
                      guid=None,
                      account_id=None,
                      brain_enabled=None)

    read_project = project.read()

    if read_project is None:
        abort(404, f'Project with id:{project_id} not found')
    else:
        schema = ProjectSchema()
        project_serialized = schema.dump(read_project)

        return project_serialized, 200

def search(user_id, account_id):
    """
    This function retrieves a list of projects based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :return: 200 on success, 404 on no projects found
    """

    existing_projects = Project.query.filter(Project.account_id == account_id).all()
    if existing_projects is None:
        abort(404, f'No projects found')

    schema = ProjectSchema(many=True)
    projects_serialized = schema.dump(existing_projects)

    return projects_serialized, 200

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

    updated_project = project.update()

    if updated_project is None:
        abort(404, f'Project {project_id} not found')
    else:
        project_serialized = schema.dump(updated_project)

        return project_serialized, 200

def delete(user_id, account_id, project_id):
    """
    This function deletes an project based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :return: 200 on success, 404 on project not found
    """

    project_to_delete = Project(id=project_id,
                                name=None,
                                guid=None,
                                account_id=None,
                                brain_enabled=None)

    if project_to_delete.delete() is not None:
        abort(404, f'Project {project_id} not found')
    else:
        return "Project deleted", 200

"""
This is the project module and supports all the ReST actions for PROJECTS
"""

from flask import abort
from configuration import db
from models.project import Project, ProjectSchema
from sqlalchemy.orm.exc import NoResultFound

def create(user_id, account_id, project):
    """
    This function creates a new project for a specific account
    of a specific user based on the passed-in project data

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project: project to create in projects structure
    :return: 201 on success, 409 on project already exists
    """

    # get provided project guid
    guid = project.get('guid')

    # validate if an project with the provided data exists
    existing_project = (Project.query.filter(Project.guid == guid)
                                     .filter(Project.account_id == account_id)
                                     .one_or_none())

    if existing_project is None:
        schema = ProjectSchema()

        # Create a project instance using the schema and the passed-in project
        new_project = schema.load(project)

        # Add the project to the database
        db.session.add(new_project)

        db.session.commit()

        # return the newly created project id in the response
        return new_project.project_id , 201

    else:
        abort(409, f'Project {guid} already exists for account {account_id}')

def read(user_id, account_id, project_id):
    """
    This function retrieves a project based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :return: 200 on success, 404 on project already exists
    """

    try:
        # get project if it exists
        existing_project = Project.query.filter(Project.project_id == project_id).one()
    except NoResultFound:
        abort(404, f'Project with id:{project_id} not found')

    schema = ProjectSchema()
    project = schema.dump(existing_project)

    return project, 200

def search(user_id, account_id):
    """
    This function retrieves a list of projects based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :return: 200 on success, 404 on no projects found
    """

    # search projects for the user and acount ids provided
    existing_projects = Project.query.filter(Project.account_id == account_id).all()
    if existing_projects is None:
        abort(404, f'No projects found')

    schema = ProjectSchema(many=True)
    projects = schema.dump(existing_projects)

    return projects, 200

def update(user_id, account_id, project_id, project):
    """
    This function updates an account based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :param project: payload information
    :return: 200 on success, 404 on project not found
    """

    try:
        # validate if project exists
        existing_project = Project.query.filter(Project.project_id == project_id).one()    
    except NoResultFound:
        abort(404, f'Project {project_id} not found')
    
    schema = ProjectSchema()

    # Create an project instance using the schema and the passed-in project
    updated_project = schema.load(project)

    # Set the id to the project we want to update
    updated_project.project_id = existing_project.project_id

    # Add the project to the database
    db.session.merge(updated_project)
    db.session.commit()

    return "Project updated", 200

def delete(user_id, account_id, project_id):
    """
    This function deletes an project based on the provided information

    :param user_id: user_id passed-in URL
    :param account_id: account_id passed-in URL
    :param project_id: project_id passed-in URL
    :return: 200 on success, 404 on project not found
    """

    try:
        # validate if project exists
        existing_project = Project.query.filter(Project.project_id == project_id).one()
    except NoResultFound:
        abort(404, f'Project {project_id} not found')

    # Add the project to the database
    db.session.delete(existing_project)
    db.session.commit()

    return "Project deleted", 200

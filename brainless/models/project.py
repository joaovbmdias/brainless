"""
Project module containing the project class and related project methods
"""

from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db
from models.task import Task
from models.template import Template
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_, and_

class Project(db.Model, Template):
    """ Project class """
    __tablename__ = 'project'

    project_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    guid = db.Column(db.String(32), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'), nullable=False)
    brain_enabled = db.Column(db.String(1), nullable=False, default='Y')
    created_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)

    tasks = db.relationship('Task', backref='project', lazy=True)

    def exists(self):
        try:
            existing_project = Project.query.filter(or_(Project.project_id == self.project_id, 
                                                         and_(Project.guid == self.guid, 
                                                              Project.account_id == self.account_id))).one()   
        except NoResultFound:
            return None

        return existing_project

class ProjectSchema(SQLAlchemyAutoSchema):
    """ ProjectSchema class """
    class Meta:
        """ Meta class classification """
        model = Project
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True

"""
Project module containing the project class and related project methods
"""

from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db
from models.task import Task

class Project(db.Model):
    """ Project class """
    __tablename__ = 'project'

    project_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    account_id = db.Column(db.Integer, db.ForeignKey('account.account_id'), nullable=False)
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    tasks = db.relationship('Task', backref='project', lazy=True)

    def __init__(self, name):
        self.project_id = None
        self.name = name
        self.__created_timestamp = datetime.utcnow
        self.__edited_timestamp = datetime.utcnow

class ProjectSchema(SQLAlchemyAutoSchema):
    """ ProjectSchema class """
    class Meta:
        """ Meta class classification """
        model = Project
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True

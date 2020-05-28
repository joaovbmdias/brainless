"""
Task module containing the task class and related task methods
"""

from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db
from models.label import Label

class Task(db.Model):
    """ Task class """
    __tablename__ = 'task'

    task_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'), nullable=False)
    due_datetime = db.Column(db.DateTime)
    priority = db.Column(db.Integer)
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    labels = db.relationship('Label', secondary='task_labels', back_populates='task')

    def __init__(self, title, project_id, due_datetime, priority):
        self.task_id = None
        self.title = title
        self.project_id = project_id
        self.due_datetime = due_datetime
        self.priority = priority
        self.__created_timestamp = datetime.utcnow
        self.__edited_timestamp = datetime.utcnow

class TaskSchema(SQLAlchemyAutoSchema):
    """ TaskSchema class """
    class Meta:
        """ Meta class classification """
        model = Task
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True

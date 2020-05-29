"""
Task module containing the task class and related task methods
"""

from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db
from models.label import Label

# task and labels association table
task_labels = db.Table('task_labels',
                        db.metadata, 
                        db.Column('task_id', db.ForeignKey('task.task_id'), primary_key=True), 
                        db.Column('label_id', db.ForeignKey('label.label_id'), primary_key=True))

class Task(db.Model):
    """ Task class """
    __tablename__ = 'task'

    task_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('project.project_id'), nullable=False)
    due_datetime = db.Column(db.DateTime, nullable=True)
    priority = db.Column(db.Integer, nullable=True)
    guid = db.Column(db.String(32), nullable=False)
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    labels = db.relationship('Label', secondary=task_labels, backref='tasks')

    def __init__(self, name, project_id, guid, due_datetime=None, priority=None):
        self.task_id = None
        self.name = name
        self.project_id = project_id
        self.due_datetime = due_datetime
        self.priority = priority
        self.guid = guid
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

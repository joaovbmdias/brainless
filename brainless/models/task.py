"""
Task module containing the task class and related task methods
"""

from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db
from models.label import Label
from models.template import Template
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_, and_

# task and labels association table
task_labels = db.Table('task_labels',
                        db.metadata, 
                        db.Column('task_id', db.ForeignKey('task.task_id'), primary_key=True), 
                        db.Column('label_id', db.ForeignKey('label.label_id'), primary_key=True))

class Task(db.Model, Template):
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

    def exists(self):

        try:
            existing_task = Task.query.filter(or_(Task.task_id == self.task_id, 
                                                  and_(Task.guid == self.guid, 
                                                  Task.project_id == self.project_id))).one()   
        except NoResultFound:
            return None

        return existing_task

    def synchronize(self):
        print('hello')

class TaskSchema(SQLAlchemyAutoSchema):
    """ TaskSchema class """
    class Meta:
        """ Meta class classification """
        model = Task
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True

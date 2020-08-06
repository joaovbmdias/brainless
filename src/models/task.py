"""
Task module containing the task class and related task methods
"""

from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db
from models.label import Label
from models.template import Template
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_, and_, UniqueConstraint

# task and labels association table
task_labels = db.Table('task_labels',
                        db.metadata, 
                        db.Column('task_id', db.ForeignKey('task.id'),   primary_key=True), 
                        db.Column('label_id', db.ForeignKey('label.id'), primary_key=True))

class Task(db.Model, Template):
    """ Task class """
    __tablename__ = 'task'

    id                  = db.Column(db.Integer,     primary_key=True)
    name                = db.Column(db.String(120), nullable=False)
    due_datetime        = db.Column(db.DateTime,    nullable=True)
    priority            = db.Column(db.Integer,     nullable=True)
    guid                = db.Column(db.String(50),  nullable=False)
    __created_timestamp = db.Column(db.DateTime,    default=datetime.utcnow)
    __edited_timestamp  = db.Column(db.DateTime,    default=datetime.utcnow,     onupdate=datetime.utcnow)
    project_id          = db.Column(db.Integer,     db.ForeignKey('project.id'), nullable=False)

    labels = db.relationship('Label', secondary=task_labels, backref='tasks')

    __table_args__ = (
        UniqueConstraint('guid', 'project_id', name='unique_guid'),
        None)

    def __init__(self, name, project_id, due_datetime, priority, guid, id=None):
        self.name         = name
        self.project_id   = project_id
        self.due_datetime = due_datetime
        self.priority     = priority
        self.guid         = guid
        self.id           = id

    def exists(self):

        try:
            existing_task = Task.query.filter(or_(Task.id         == self.id, 
                                                  and_(Task.guid  == self.guid, 
                                                  Task.project_id == self.project_id))).one()   
        except NoResultFound:
            return None

        return existing_task

class TaskSchema(SQLAlchemyAutoSchema):
    """ TaskSchema class """
    class Meta:
        """ Meta class classification """
        model                 = Task
        sqla_session          = db.session
        include_fk            = True
        include_relationships = True
        load_instance         = True

"""
Label module containing the label class and related label methods
"""

from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db
from sqlalchemy import Table, Text

# task and labels association table
task_labels = Table('task_labels',
                    db.metadata, 
                    Column('task_id', ForeignKey('task.task_id'), primary_key=True), 
                    Column('label_id', ForeignKey('label.label_id'), primary_key=True))


class Label(db.Model):
    """ Label class """
    __tablename__ = 'label'

    label_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    labels = db.relationship('Label', secondary='task_labels', back_populates='label')

    def __init__(self, title, project_id, due_datetime, priority):
        self.task_id = None
        self.title = title
        self.project_id = project_id
        self.due_datetime = due_datetime
        self.priority = priority
        self.__created_timestamp = datetime.utcnow
        self.__edited_timestamp = datetime.utcnow

class LabelSchema(SQLAlchemyAutoSchema):
    """ LabelSchema class """
    class Meta:
        """ Meta class classification """
        model = Label
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True

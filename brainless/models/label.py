"""
Label module containing the label class and related label methods
"""

from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db

class Label(db.Model):
    """ Label class """
    __tablename__ = 'label'

    label_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(32), nullable=False)
    guid = db.Column(db.String(32), nullable=False)
    account_id = db.Column(db.Integer)
    created_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, title, guid, account_id):
        self.label_id = None
        self.title = title
        self.guid = guid
        self.account_id = account_id
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

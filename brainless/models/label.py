"""
Label module containing the label class and related label methods
"""

from datetime import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration import db
from models.template import Template
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import or_, and_

class Label(db.Model, Template):
    """ Label class """
    __tablename__ = 'label'

    label_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    guid = db.Column(db.String(32), nullable=False)
    account_id = db.Column(db.Integer, nullable=False)
    brain_enabled = db.Column(db.String(1), nullable=False, default='Y')
    created_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    edited_timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def exists(self):

        try:
            existing_label = Label.query.filter(or_(Label.label_id == self.label_id, 
                                                    and_(Label.guid == self.guid, 
                                                         Label.account_id == self.account_id))).one()   
        except NoResultFound:
            return None

        return existing_label


class LabelSchema(SQLAlchemyAutoSchema):
    """ LabelSchema class """
    class Meta:
        """ Meta class classification """
        model = Label
        sqla_session = db.session
        include_fk = True
        include_relationships = True
        load_instance = True

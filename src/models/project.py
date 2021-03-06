"""
Project module containing the project class and related project methods
"""

from datetime               import datetime
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from configuration          import db
from models.task            import Task
from models.template        import Template
from sqlalchemy.orm.exc     import NoResultFound
from sqlalchemy             import or_, and_, CheckConstraint, UniqueConstraint

class Project(db.Model, Template):
    """ Project class """
    __tablename__ = 'project'

    id                  = db.Column(db.Integer,    primary_key=True)
    name                = db.Column(db.String(50), nullable=False)
    guid                = db.Column(db.String(50), nullable=False)
    brain_enabled       = db.Column(db.String(1),  nullable=False, default='Y')
    __created_timestamp = db.Column(db.DateTime,   nullable=False, default=datetime.utcnow)
    __edited_timestamp  = db.Column(db.DateTime,   nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow)
    account_id          = db.Column(db.Integer,    db.ForeignKey('account.id'),             nullable=False)

    tasks = db.relationship('Task', backref='project', lazy=True, cascade="save-update, merge, delete")

    __table_args__ = (
        CheckConstraint('brain_enabled IN (\'Y\', \'N\')', name='brain_enabled_val'),
        UniqueConstraint('guid', 'account_id', name='unique_guid'))

    def __init__(self, name, guid, account_id, brain_enabled='Y', id=None):
        self.name          = name
        self.guid          = guid
        self.account_id    = account_id
        self.brain_enabled = brain_enabled
        self.id            = id

    def exists(self):
        try:
            existing_project = Project.query.filter(or_(Project.id            == self.id, 
                                                      and_(Project.guid       == self.guid, 
                                                           Project.account_id == self.account_id))
                                                   ).one()   
        except NoResultFound:
            return None

        return existing_project

    def synchronize(self, tasks):

        if self.id is None:
            self.create()
        else:
            self.update()

        task_guids = []

        if self.brain_enabled:

            if tasks is not None:
                for ta in tasks:
                    local = Task(id           = None,
                                 name         = ta['name'],
                                 guid         = ta['guid'],
                                 priority     = ta['priority'],
                                 due_datetime = ta['due_datetime'],
                                 project_id   = self.id)

                    task = local.read()

                    if task is not None:
                        local.id = task.id
    
                    task = local
                    task.synchronize()

                    task_guids.append(ta['guid'])

        for ta in Task.query.filter(and_(Task.project_id == self.id, ~Task.guid.in_(task_guids))).all():
            db.session.delete(ta)

class ProjectSchema(SQLAlchemyAutoSchema):
    """ ProjectSchema class """
    class Meta:
        """ Meta class classification """
        model                 = Project
        sqla_session          = db.session
        include_fk            = True
        include_relationships = True
        load_instance         = True

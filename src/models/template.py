from datetime import datetime
from configuration import db
from constants import SUCCESS, FAILURE

class Template():
    """ Template class """

    def exists(self):
        return self

    def create(self, bypass_commit=False):
        """
        Core Create
        """
        if self.exists() is None:
            try:
                db.session.add(self)
                if not bypass_commit:
                    db.session.commit()
            except:
                db.session.rollback()
                return FAILURE
            return SUCCESS
        else:
            return FAILURE

    def read(self):
        """
        Core Read
        """
        self = self.exists()

        if self is not None:
            return SUCCESS
        else:
            return FAILURE

    def update(self, bypass_commit=False):
        """
        Core Update
        """
        if self.exists() is not None:
            try:
                db.session.merge(self)
                if not bypass_commit:
                    db.session.commit()
            except:
                db.session.rollback()
                return FAILURE
            return SUCCESS
        else:
            return FAILURE

    def delete(self, bypass_commit=False):
        """
        Core Delete
        """        
        existing = self.exists()
        if existing is not None:
            db.session.delete(existing)
            if not bypass_commit:
                db.session.commit()
            return SUCCESS
        else:
            return FAILURE

    def synchronize(self):
        """
        Core Synchronize
        """
        if self.id is None:
            self.create(bypass_commit=True)
        else:
            self.update(bypass_commit=True)

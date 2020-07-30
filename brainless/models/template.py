from datetime import datetime
from configuration import db

class Template():
    """ Template class """

    def exists(self):

        return self

    def create(self, bypass_commit=False):
        """
        Core Create
        """

        if self.exists() is None:
            # add the template to the database
            db.session.add(self)
            if not bypass_commit:
                db.session.commit()

            return self

        else:
            return None

    def read(self):
        """
        Core Read
        """

        self = self.exists()

        return self

    def update(self, bypass_commit=False):
        """
        Core Update
        """

        existing = self.exists()

        if existing.id is not None:
            # Update the template in the database
            #self.id = existing.id

            db.session.merge(self)
            if not bypass_commit:
                db.session.commit()

            return self

        else:
            return None

    def delete(self, bypass_commit=False):
        """
        Core Delete
        """        
        
        existing_template = self.exists()

        if existing_template is not None:
            db.session.delete(existing_template)
            if not bypass_commit:
                db.session.commit()

            return None
        else:
            return self

    def synchronize(self):
        """
        Core Synchronize
        """

        if self.id is None:
            self.create(bypass_commit=True)
        else:
            self.update(bypass_commit=True)
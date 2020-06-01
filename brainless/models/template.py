from datetime import datetime
from configuration import db

class Template():
    """ Template class """

    def exists(self):

        return self

    def create(self):
        """
        Core Create
        """

        if self.exists() is None:
            # add the template to the database
            db.session.add(self)
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

    def update(self):
        """
        Core Update
        """

        if self.exists():
            # Update the template in the database
            db.session.merge(self)
            db.session.commit()

            return self

        else:
            return None

    def delete(self):
        """
        Core Delete
        """        
        
        existing_template = self.exists()

        if existing_template is not None:
            db.session.delete(existing_template)
            db.session.commit()

            return None
        else:
            return self

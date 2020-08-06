import unittest
import constants
from configuration import db
from models.project import Project

db.metadata.create_all(db.engine)
unittest.TestLoader.sortTestMethodsUsing = None

class TestProject(unittest.TestCase):
    def test_1_1_create_project(self):
        """
        Test that it can create a project
        """
        project = Project(name          = "Awesome Project",
                          guid          = "arghdlaijsbfzsdjhgfoqeiugtoiweg",
                          account_id    = 1,
                          brain_enabled = "Y")

        result = project.create()

        self.assertIsNotNone(project.id, "Project ID cannot be None")
        self.assertGreater(project.id, 0, "Project ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_1_2_create_another_project(self):
        """
        Test that it can create another project
        """
        project = Project(name          = "An even more awesome project",
                          guid          = "adfhsdykluiglçoçõuryirtyuetutrh",
                          account_id    = 1,
                          brain_enabled = "Y")

        result = project.create()

        self.assertIsNotNone(project.id, "Project ID cannot be None")
        self.assertGreater(project.id, 0, "Project ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_1_3_create_yet_another_project(self):
        """
        Test that it can create a third project
        """
        project = Project(name          = "Cool awesome Project",
                          guid          = "sykt5ywtrshatrusns",
                          account_id    = 1,
                          brain_enabled = "Y")

        result = project.create()

        self.assertIsNotNone(project.id, "Project ID cannot be None")
        self.assertGreater(project.id, 0, "Project ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_2_1_create_same_project(self):
        """
        Test that it cannot create an existing project
        """
        project = Project(name          = "Awesome Project",
                          guid          = "arghdlaijsbfzsdjhgfoqeiugtoiweg",
                          account_id    = 1,
                          brain_enabled = "Y")

        result = project.create()

        self.assertIsNone(project.id, "Project ID must be None")
        self.assertEqual(result, constants.FAILURE)

    def test_3_1_delete_existing_project(self):
        """
        Test that it can delete an existing project
        """   
        project = Project(name          = "Cool awesome Project",
                          guid          = "sykt5ywtrshatrusns",
                          account_id    = 1,
                          brain_enabled = "Y",
                          id            = 3)

        result = project.delete()

        self.assertEqual(result, constants.SUCCESS)

    def test_3_2_delete_unexisting_project(self):
        """
        Test that it cannot delete an unexisting project
        """
        project = Project(name          = "Cool awesome Project",
                          guid          = "fsdhjsdtkusygjsgdkuly",
                          account_id    = 1,
                          brain_enabled = "Y",
                          id            = 100000)

        result = project.delete()

        self.assertEqual(result, constants.FAILURE)

    def test_4_1_read_one_existing_project(self):
        """
        Test that it can read an existing project
        """
        project = Project(name          = None,
                          guid          = None,
                          account_id    = None,
                          brain_enabled = None,
                          id            = 1)

        result = project.read()

        self.assertEqual(result, constants.SUCCESS)

    def test_4_2_read_one_unexisting_project(self):
        """
        Test that it cannot read an unexisting project
        """
        project = Project(name          = None,
                          guid          = None,
                          account_id    = None,
                          brain_enabled = None,
                          id            = 100000)

        result = project.read()

        self.assertEqual(result, constants.FAILURE)

    def test_5_1_update_existing_project(self):
        """
        Test that it can update an existing project
        """
        project = Project(name          = "An even more awesome project UPDATED",
                          guid          = "adfhsdykluiglçoçõuryirtyuetutrh",
                          account_id    = 1,
                          brain_enabled = "Y",
                          id            = 2)

        result = project.update()

        self.assertEqual(result, constants.SUCCESS)

    def test_5_2_update_unexisting_project(self):
        """
        Test that it cannot update an unexisting account
        """
        project = Project(name          = "A random project",
                          guid          = "aehrtjsrhrtjsrtjr",
                          account_id    = 1,
                          brain_enabled = "Y",
                          id            = 10000000)

        result = project.update()

        self.assertEqual(result, constants.FAILURE)

    def test_6_1_check_project_brain_val(self):
        """
        Test that it cannot create a project with brain value not in (Y,N)
        """
        project = Project(name          = "Awesome Project Check",
                          guid          = "arghdlaijsbfzsdjhgfoqeiugtoiweg",
                          account_id    = 1,
                          brain_enabled = "X")

        result = project.create()

        self.assertEqual(result, constants.FAILURE)

if __name__ == '__main__':
    db.metadata.create_all(db.engine)
    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()

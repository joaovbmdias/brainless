import unittest
import constants
from configuration import db
from models.task import Task
from datetime import datetime

db.metadata.create_all(db.engine)
unittest.TestLoader.sortTestMethodsUsing = None

class TestTask(unittest.TestCase):
    def test_1_1_create_task(self):
        """
        Test that it can create a task
        """
        task = Task(name = "Amazing task",
                    project_id = 1,
                    due_datetime = datetime.strptime("2020-05-29 20:00", '%Y-%m-%d %H:%M'),
                    priority = 1,
                    guid = "asdvakjfhvaskfasvfkasvfkjasv")

        result = task.create()

        self.assertIsNotNone(task.id, "Task ID cannot be None")
        self.assertGreater(task.id, 0, "Task ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_1_2_create_another_task(self):
        """
        Test that it can create another task
        """
        task = Task(name = "Another Amazing task",
                    project_id = 1,
                    due_datetime = datetime.strptime("2020-05-29 20:00", '%Y-%m-%d %H:%M'),
                    priority = 1,
                    guid = "asdgflkjnadrkçgjbadkçgb")

        result = task.create()

        self.assertIsNotNone(task.id, "Task ID cannot be None")
        self.assertGreater(task.id, 0, "Task ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_1_3_create_yet_another_task(self):
        """
        Test that it can create a third task
        """
        task = Task(name = "A Third Amazing task",
                    project_id = 1,
                    due_datetime = datetime.strptime("2020-05-29 20:00", '%Y-%m-%d %H:%M'),
                    priority = 1,
                    guid = "aegpoiasenpgadrgpsdngao")

        result = task.create()

        self.assertIsNotNone(task.id, "Task ID cannot be None")
        self.assertGreater(task.id, 0, "Task ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_2_1_create_same_task(self):
        """
        Test that it cannot create an existing task
        """
        task = Task(name = "Amazing task",
                    project_id = 1,
                    due_datetime = datetime.strptime("2020-05-29 20:00", '%Y-%m-%d %H:%M'),
                    priority = 1,
                    guid = "asdvakjfhvaskfasvfkasvfkjasv")

        result = task.create()

        self.assertIsNone(task.id, "Task ID must be None")
        self.assertEqual(result, constants.FAILURE)

    def test_3_1_delete_existing_task(self):
        """
        Test that it can delete an existing task
        """
        task = Task(name = None,
                    project_id = None,
                    due_datetime = None,
                    priority = None,
                    guid = None,
                    id   = 3)

        result = task.delete()

        self.assertEqual(result, constants.SUCCESS)

    def test_3_2_delete_unexisting_task(self):
        """
        Test that it cannot delete an unexisting task
        """
        task = Task(name = None,
                    project_id = None,
                    due_datetime = None,
                    priority = None,
                    guid = None,
                    id   = 1000000)

        result = task.delete()

        self.assertEqual(result, constants.FAILURE)

    def test_4_1_read_one_existing_task(self):
        """
        Test that it can read an existing task
        """
        task = Task(name = None,
                    project_id = None,
                    due_datetime = None,
                    priority = None,
                    guid = None,
                    id   = 1)

        result = task.read()

        self.assertEqual(result, constants.SUCCESS)
        self.assertIsNotNone(task.id, "Task ID cannot be None")
        self.assertGreater(task.id, 0, "Task ID must be greater than 0")

    def test_4_2_read_one_unexisting_task(self):
        """
        Test that it cannot read an unexisting task
        """
        task = Task(name = None,
                    project_id = None,
                    due_datetime = None,
                    priority = None,
                    guid = None,
                    id   = 1000000)

        result = task.read()

        self.assertEqual(result, constants.FAILURE)

    def test_5_1_update_existing_task(self):
        """
        Test that it can update an existing task
        """
        task = Task(name = "Amazing task UPDATED",
                    project_id = 1,
                    due_datetime = datetime.strptime("2020-05-29 20:00", '%Y-%m-%d %H:%M'),
                    priority = 1,
                    guid = "asdvakjfhvaskfasvfkasvfkjasv",
                    id = 1)

        result = task.update()

        self.assertEqual(result, constants.SUCCESS)

    def test_5_2_update_unexisting_task(self):
        """
        Test that it cannot update an unexisting account
        """
        task = Task(name = "Amazingly Awkward task UPDATED",
                    project_id = 1,
                    due_datetime = datetime.strptime("2020-05-29 20:00", '%Y-%m-%d %H:%M'),
                    priority = 1,
                    guid = "weryhwrethçaekrsjngsrlthpri",
                    id = 10000)

        result = task.update()

        self.assertEqual(result, constants.FAILURE)

if __name__ == '__main__':
    db.metadata.create_all(db.engine)
    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()

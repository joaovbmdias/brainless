import unittest
import constants
from configuration import db
from models.calendar import Calendar

db.metadata.create_all(db.engine)
unittest.TestLoader.sortTestMethodsUsing = None

class TestCalendar(unittest.TestCase):
    """
    Unit Testing Calendars
    """
    def test_1_1_create_calendar(self):
        """
        Test that it can create a calendar
        """
        calendar = Calendar(name          = "Awesome Calendar",
                            guid          = "arghdlaijsbfzsdjhgfoqeiugtoiweg",
                            account_id    = 1,
                            brain_enabled = "Y")

        result = calendar.create()

        self.assertIsNotNone(calendar.id, "Calendar ID cannot be None")
        self.assertGreater(calendar.id, 0, "Calendar ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_1_2_create_another_calendar(self):
        """
        Test that it can create another calendar
        """
        calendar = Calendar(name          = "An even more awesome calendar",
                            guid          = "astjkdudyutsuklryidyt",
                            account_id    = 1,
                            brain_enabled = "Y")

        result = calendar.create()

        self.assertIsNotNone(calendar.id, "Calendar ID cannot be None")
        self.assertGreater(calendar.id, 0, "Calendar ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_1_3_create_yet_another_calendar(self):
        """
        Test that it can create a third calendar
        """
        calendar = Calendar(name          = "Cool awesome Calendar",
                            guid          = "fiyiydutdiyuogouygoihiohuoiyfutrdyt",
                            account_id    = 1,
                            brain_enabled = "Y")

        result = calendar.create()

        self.assertIsNotNone(calendar.id, "Calendar ID cannot be None")
        self.assertGreater(calendar.id, 0, "Calendar ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_2_1_create_same_calendar(self):
        """
        Test that it cannot create an existing calendar
        """
        calendar = Calendar(name          = "Awesome Calendar",
                            guid          = "arghdlaijsbfzsdjhgfoqeiugtoiweg",
                            account_id    = 1,
                            brain_enabled = "Y")

        result = calendar.create()

        self.assertIsNone(calendar.id, "Calendar ID must be None")
        self.assertEqual(result, constants.FAILURE)

    def test_3_1_delete_existing_calendar(self):
        """
        Test that it can delete an existing calendar
        """   
        calendar = Calendar(name          = "Cool awesome Calendar",
                            guid          = "fiyiydutdiyuogouygoihiohuoiyfutrdyt",
                            account_id    = 1,
                            brain_enabled = "Y",
                            id            = 3)

        result = calendar.delete()

        self.assertEqual(result, constants.SUCCESS)

    def test_3_2_delete_unexisting_calendar(self):
        """
        Test that it cannot delete an unexisting calendar
        """
        calendar = Calendar(name          = "Cool awesome Calendar",
                            guid          = "fsdhjsdtkusygjsgdkuly",
                            account_id    = 1,
                            brain_enabled = "Y",
                            id            = 100000)

        result = calendar.delete()

        self.assertEqual(result, constants.FAILURE)

    def test_4_1_read_one_existing_calendar(self):
        """
        Test that it can read an existing calendar
        """
        calendar = Calendar(name          = None,
                            guid          = None,
                            account_id    = None,
                            brain_enabled = None,
                            id            = 1)

        result = calendar.read()

        self.assertEqual(result, constants.SUCCESS)

    def test_4_2_read_one_unexisting_calendar(self):
        """
        Test that it cannot read an unexisting calendar
        """
        calendar = Calendar(name          = None,
                            guid          = None,
                            account_id    = None,
                            brain_enabled = None,
                            id            = 100000)

        result = calendar.read()

        self.assertEqual(result, constants.FAILURE)

    def test_5_1_update_existing_calendar(self):
        """
        Test that it can update an existing calendar
        """
        calendar = Calendar(name          = "An even more awesome calendar UPDATED",
                            guid          = "astjkdudyutsuklryidyt",
                            account_id    = 1,
                            brain_enabled = "Y",
                            id            = 2)

        result = calendar.update()

        self.assertEqual(result, constants.SUCCESS)

    def test_5_2_update_unexisting_calendar(self):
        """
        Test that it cannot update an unexisting account
        """
        calendar = Calendar(name          = "A random calendar",
                            guid          = "aehrtjsrhrtjsrtjr",
                            account_id    = 1,
                            brain_enabled = "Y",
                            id            = 10000000)

        result = calendar.update()

        self.assertEqual(result, constants.FAILURE)

    def test_6_1_check_calendar_brain_val(self):
        """
        Test that it cannot create a calendar with brain value not in (Y,N)
        """
        calendar = Calendar(name          = "Awesome Calendar Check",
                            guid          = "arghdlaijsbfzsdjhgfoqeiugtoiweg",
                            account_id    = 1,
                            brain_enabled = "X")

        result = calendar.create()

        self.assertEqual(result, constants.FAILURE)

if __name__ == '__main__':
    db.metadata.create_all(db.engine)
    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()

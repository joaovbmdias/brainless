import unittest
import constants
from configuration import db
from models.event import Event
from datetime import datetime

db.metadata.create_all(db.engine)
unittest.TestLoader.sortTestMethodsUsing = None

class TestEvent(unittest.TestCase):
    """
    Unit Testing Events
    """
    def test_1_1_create_event(self):
        """
        Test that it can create a event
        """
        event = Event(name           = "Awesome Event",
                      start_datetime = datetime.strptime("2020-05-22 20:00", '%Y-%m-%d %H:%M'),
                      end_datetime   = datetime.strptime("2020-05-22 22:00", '%Y-%m-%d %H:%M'),
                      guid           = "arghdlaijsbfzsdjhgfoqeiugtoiweg",
                      calendar_id    = 1)

        result = event.create()

        self.assertIsNotNone(event.id, "Event ID cannot be None")
        self.assertGreater(event.id, 0, "Event ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_1_2_create_another_event(self):
        """
        Test that it can create another event
        """
        event = Event(name           = "Another Awesome Event",
                      start_datetime = datetime.strptime("2020-05-22 21:00", '%Y-%m-%d %H:%M'),
                      end_datetime   = datetime.strptime("2020-05-22 23:00", '%Y-%m-%d %H:%M'),
                      guid           = "arehsyidtiryotuoytusrtyarts",
                      calendar_id    = 1)

        result = event.create()

        self.assertIsNotNone(event.id, "Event ID cannot be None")
        self.assertGreater(event.id, 0, "Event ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_1_3_create_yet_another_event(self):
        """
        Test that it can create a third event
        """
        event = Event(name           = "Yet Another Awesome Event",
                      start_datetime = datetime.strptime("2020-05-22 20:00", '%Y-%m-%d %H:%M'),
                      end_datetime   = datetime.strptime("2020-05-22 22:00", '%Y-%m-%d %H:%M'),
                      guid           = "skldyfrstjdtiftu9piuryaestd",
                      calendar_id    = 1)

        result = event.create()

        self.assertIsNotNone(event.id, "Event ID cannot be None")
        self.assertGreater(event.id, 0, "Event ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_2_1_create_same_event(self):
        """
        Test that it cannot create an existing event
        """
        event = Event(name           = "Awesome Event",
                      start_datetime = datetime.strptime("2020-05-22 20:00", '%Y-%m-%d %H:%M'),
                      end_datetime   = datetime.strptime("2020-05-22 22:00", '%Y-%m-%d %H:%M'),
                      guid           = "arghdlaijsbfzsdjhgfoqeiugtoiweg",
                      calendar_id    = 1)

        result = event.create()

        self.assertIsNone(event.id, "Event ID must be None")
        self.assertEqual(result, constants.FAILURE)

    def test_3_1_delete_existing_event(self):
        """
        Test that it can delete an existing event
        """
        event = Event(name           = "Yet Another Awesome Event",
                      start_datetime = datetime.strptime("2020-05-22 20:00", '%Y-%m-%d %H:%M'),
                      end_datetime   = datetime.strptime("2020-05-22 22:00", '%Y-%m-%d %H:%M'),
                      guid           = "skldyfrstjdtiftu9piuryaestd",
                      calendar_id    = 1,
                      id             = 3)

        result = event.delete()

        self.assertEqual(result, constants.SUCCESS)

    def test_3_2_delete_unexisting_event(self):
        """
        Test that it cannot delete an unexisting event
        """
        event = Event(name           = "Random Event",
                      start_datetime = datetime.strptime("2020-05-22 20:00", '%Y-%m-%d %H:%M'),
                      end_datetime   = datetime.strptime("2020-05-22 22:00", '%Y-%m-%d %H:%M'),
                      guid           = "sjkdyfltut8i6ywersdnf",
                      calendar_id    = 1,
                      id             = 100000)

        result = event.delete()

        self.assertEqual(result, constants.FAILURE)

    def test_4_1_read_one_existing_event(self):
        """
        Test that it can read an existing event
        """
        event = Event(name           = None,
                      start_datetime = None,
                      end_datetime   = None,
                      guid           = None,
                      calendar_id    = None,
                      id             = 1)

        result = event.read()

        self.assertEqual(result, constants.SUCCESS)

    def test_4_2_read_one_unexisting_event(self):
        """
        Test that it cannot read an unexisting event
        """
        event = Event(name           = None,
                      start_datetime = None,
                      end_datetime   = None,
                      guid           = None,
                      calendar_id    = None,
                      id             = 100000)

        result = event.read()

        self.assertEqual(result, constants.FAILURE)

    def test_5_1_update_existing_event(self):
        """
        Test that it can update an existing event
        """
        event = Event(name           = "Awesome Event UPDATED",
                      start_datetime = datetime.strptime("2020-05-22 20:00", '%Y-%m-%d %H:%M'),
                      end_datetime   = datetime.strptime("2020-05-22 22:00", '%Y-%m-%d %H:%M'),
                      guid           = "arghdlaijsbfzsdjhgfoqeiugtoiweg",
                      calendar_id    = 1,
                      id             = 1)

        result = event.update()

        self.assertEqual(result, constants.SUCCESS)

    def test_5_2_update_unexisting_event(self):
        """
        Test that it cannot update an unexisting event
        """
        event = Event(name           = "Awkwardly Awesome Event",
                      start_datetime = datetime.strptime("2020-05-22 20:00", '%Y-%m-%d %H:%M'),
                      end_datetime   = datetime.strptime("2020-05-22 22:00", '%Y-%m-%d %H:%M'),
                      guid           = "arghdlaijsbfzsdjhgfoqeiugtoiweg",
                      calendar_id    = 1,
                      id             = 100000)

        result = event.update()

        self.assertEqual(result, constants.FAILURE)

if __name__ == '__main__':
    db.metadata.create_all(db.engine)
    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()

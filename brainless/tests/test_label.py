import unittest
import constants
from configuration import db
from models.label import Label

db.metadata.create_all(db.engine)
unittest.TestLoader.sortTestMethodsUsing = None

class TestLabel(unittest.TestCase):
    def test_1_1_create_label(self):
        """
        Test that it can create a label
        """
        label = Label(name          = "Amazing label",
                      guid          = "we4987twt98c4978qtc93y",
                      account_id    = 1,
                      brain_enabled = "Y",
                      order         = 1)

        result = label.create()

        self.assertIsNotNone(label.id, "Label ID cannot be None")
        self.assertGreater(label.id, 0, "Label ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_1_2_create_another_label(self):
        """
        Test that it can create another label
        """
        label = Label(name          = "Better label",
                      guid          = "agrasrhytjky",
                      account_id    = 1,
                      brain_enabled = "Y",
                      order         = 2)

        result = label.create()

        self.assertIsNotNone(label.id, "Label ID cannot be None")
        self.assertGreater(label.id, 0, "Label ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_1_3_create_yet_another_label(self):
        """
        Test that it can create a third label
        """
        label = Label(name          = "Greater label",
                      guid          = "aesthjdytjytkfyuglkfyj",
                      account_id    = 1,
                      brain_enabled = "Y",
                      order         = 3)

        result = label.create()

        self.assertIsNotNone(label.id, "Label ID cannot be None")
        self.assertGreater(label.id, 0, "Label ID must be greater than 0")
        self.assertEqual(result, constants.SUCCESS)

    def test_2_1_create_same_label(self):
        """
        Test that it cannot create an existing label
        """
        label = Label(name          = "Amazing label",
                      guid          = "we4987twt98c4978qtc93y",
                      account_id    = 1,
                      brain_enabled = "Y",
                      order         = 1)

        result = label.create()

        self.assertIsNone(label.id, "Label ID must be None")
        self.assertEqual(result, constants.FAILURE)

    def test_3_1_delete_existing_label(self):
        """
        Test that it can delete an existing label
        """
        label = Label(name          = None,
                      guid          = None,
                      account_id    = None,
                      brain_enabled = None,
                      order         = None,
                      id            = 3)

        result = label.delete()

        self.assertEqual(result, constants.SUCCESS)

    def test_3_2_delete_unexisting_label(self):
        """
        Test that it cannot delete an unexisting label
        """
        label = Label(name          = None,
                      guid          = None,
                      account_id    = None,
                      brain_enabled = None,
                      order         = None,
                      id            = 1000000)

        result = label.delete()

        self.assertEqual(result, constants.FAILURE)

    def test_4_1_read_one_existing_label(self):
        """
        Test that it can read an existing label
        """
        label = Label(name          = None,
                      guid          = None,
                      account_id    = None,
                      brain_enabled = None,
                      order         = None,
                      id            = 1)

        result = label.read()

        self.assertEqual(result, constants.SUCCESS)
        self.assertIsNotNone(label.id, "Label ID cannot be None")
        self.assertGreater(label.id, 0, "Label ID must be greater than 0")

    def test_4_2_read_one_unexisting_label(self):
        """
        Test that it cannot read an unexisting label
        """
        label = Label(name          = None,
                      guid          = None,
                      account_id    = None,
                      brain_enabled = None,
                      order         = None,
                      id            = 1000000)

        result = label.read()

        self.assertEqual(result, constants.FAILURE)

    def test_5_1_update_existing_label(self):
        """
        Test that it can update an existing label
        """
        label = Label(name          = "Amazing label UPDATED",
                      guid          = "we4987twt98c4978qtc93y",
                      account_id    = 1,
                      brain_enabled = "Y",
                      order         = 1,
                      id            = 1)

        result = label.update()

        self.assertEqual(result, constants.SUCCESS)

    def test_5_2_update_unexisting_label(self):
        """
        Test that it cannot update an unexisting account
        """
        label = Label(name          = "Amazingle Awkward label UPDATED",
                      guid          = "agrstuedutfiy",
                      account_id    = 1,
                      brain_enabled = "Y",
                      order         = 4,
                      id            = 100000)

        result = label.update()

        self.assertEqual(result, constants.FAILURE)

    def test_6_1_check_label_brain_val(self):
        """
        Test that it cannot create a label with brain value not in (Y,N)
        """
        label = Label(name          = "Last Amazing label",
                      guid          = "sdfghdfnn",
                      account_id    = 1,
                      brain_enabled = "X",
                      order         = 10)

        result = label.create()

        self.assertEqual(result, constants.FAILURE)

if __name__ == '__main__':
    db.metadata.create_all(db.engine)
    unittest.TestLoader.sortTestMethodsUsing = None
    unittest.main()

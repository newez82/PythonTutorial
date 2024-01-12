"""
    Unit Test method never run each test in order from top to bottom.
    We should keep test isolute from one another.
"""
import unittest
from unittest.mock import patch

from employee import Employee


class TestEmployee(unittest.TestCase):
    """Unit Test Employee class"""

    # Use classmethod to run at the beginning of the test and
    # clean up code that runs after the all the test have
    # been run.
    # i.e. connect to database and close database
    @classmethod
    def setUpClass(cls):
        """setup Class"""
        print("setup Class")

    @classmethod
    def tearDownClass(cls):
        """tearDown Class"""
        print("tear Down Class")

    def setUp(self):
        print("setUp")
        self.emp_1 = Employee("Corey", "Schafer", 50000)
        self.emp_2 = Employee("Sue", "Smith", 60000)

    def tearDown(self):
        print("tearDown\n")

    def test_email(self):
        """test email"""
        print("test email")
        self.assertEqual(self.emp_1.email, "Corey.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Sue.Smith@email.com")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.email, "John.Schafer@email.com")
        self.assertEqual(self.emp_2.email, "Jane.Smith@email.com")

    def test_fullname(self):
        """test full name"""
        print("test full name")
        self.assertEqual(self.emp_1.fullname, "Corey Schafer")
        self.assertEqual(self.emp_2.fullname, "Sue Smith")

        self.emp_1.first = "John"
        self.emp_2.first = "Jane"

        self.assertEqual(self.emp_1.fullname, "John Schafer")
        self.assertEqual(self.emp_2.fullname, "Jane Smith")

    def test_apply_raise(self):
        """test apply raise"""
        print("test apply raise")
        self.emp_1.apply_raise()
        self.emp_2.apply_raise()

        self.assertEqual(self.emp_1.pay, 52500)
        self.assertEqual(self.emp_2.pay, 63000)

    def test_monthly_schedule(self):
        """test monthly schedule"""
        # use patch in context manager to mock to service
        with patch("employee.requests.get") as mocked_get:
            mocked_get.return_value.ok = True
            mocked_get.return_value.text = "Success"

            schedule = self.emp_1.monthly_schedule("May")
            # make sure the get method is called with correct URL
            mocked_get.assert_called_with("http://company.com/Schafer/May", timeout=10)
            self.assertEqual(schedule, "Success")

            mocked_get.return_value.ok = False

            schedule = self.emp_2.monthly_schedule("June")
            mocked_get.assert_called_with("http://company.com/Smith/June", timeout=10)
            self.assertEqual(schedule, "Bad Response!")


if __name__ == "__main__":
    unittest.main()

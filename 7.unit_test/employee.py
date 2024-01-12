"""
    Employee class for unit test
"""
import requests


class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):
        """return email"""
        return f"{self.first}.{self.last}@email.com"

    @property
    def fullname(self):
        """return full name"""
        return f"{self.first} {self.last}"

    def apply_raise(self):
        """calculate raise"""
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):
        """return monthly schedule"""
        response = requests.get(f"http://company.com/{self.last}/{month}", timeout=10)
        if response.ok:
            return response.text
        else:
            return "Bad Response!"

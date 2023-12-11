"""
Main code file
"""
from data import DataBase

db = DataBase()


class Generator:
    """
    Generator class for custom data.
    """

    def __init__(self):
        pass

    def generate_cars(self):
        """_summary_
        """

    def generate_drivers(self):
        """_summary_
        """

    def generate_violations(self):
        """_summary_
        """

    def generate_fine(self):
        """_summary_
        """


if __name__ == "main":
    gen = Generator()

    for car in gen.generate_cars():
        db.cars.insert()

    for driver in gen.generate_drivers():
        db.drivers.insert()

    for fine in gen.generate_fine():
        db.fine.insert()

    for violation in gen.generate_violations():
        db.violations.insert()

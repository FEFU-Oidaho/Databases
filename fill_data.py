"""
Main code file
"""

import random
from data import DataBase


class Generator:
    """
    Generator class for custom data.
    """

    def __init__(self):
        self.db = DataBase()

        self.names = ["Русалан", "Владимир", "Юрий", "Антон", "Александр"]
        self.surnames = ["Соловьев", "Крапов", "Коробочкин", "Крутышов"]
        self.thirdname = ["Владимирович", "Олегович", "Рюрикович", "Романович"]

        self.cities = ["г. Владивосток", "г. Артём", "г. Большой камень"]
        self.streets = ["ул. Давыдова", "ул. Петровского", "ул. Карла Маркса"]

    def generate_cars(self):
        """_summary_
        """

    def generate_drivers(self, entity_count: int = 10):
        """_summary_
        """
        drivers = []

        for i in range(0, entity_count):
            license_number = random.randint(1, 228)

            name = self.names[random.randint(0, len(self.names)-1)]
            surname = self.surnames[random.randint(0, len(self.surnames)-1)]
            thirdname = self.thirdname[random.randint(0, len(self.thirdname)-1)]
            full_name = " ".join([name, surname, thirdname])

            city = self.cities[random.randint(0, len(self.cities)-1)]
            street = self.streets[random.randint(0, len(self.streets)-1)]
            house = f"д. {random.randint(0,99)}"
            address = ", ".join([city, street, house])

            phone_number = f"{random.randint(100000,999999)}"

            drivers.append(
                {
                    "license_number": license_number,
                    "full_name": full_name,
                    "address": address,
                    "phone_number": phone_number
                }
            )

        return drivers

    def generate_violations(self):
        """_summary_
        """

    def generate_fine(self):
        """_summary_
        """


if __name__ == "__main__":
    gen = Generator()

    for driver in gen.generate_drivers():
        print(driver)
        gen.db.drivers.insert(
            on_duplicate="update",
            license_number=driver.get("license_number"),
            full_name=driver.get("full_name"),
            address=driver.get("address"),
            phone_number=driver.get("phone_number")
        )
        
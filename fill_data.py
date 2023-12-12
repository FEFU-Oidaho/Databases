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
            print(i)
            driver_license = random.randint(1, 228)

            name = self.names[random.randint(0, len(self.names))]
            surname = self.surnames[random.randint(0, len(self.surnames))]
            thirdname = self.thirdname[random.randint(0, len(self.thirdname))]
            full_name = " ".join([name, surname, thirdname])

            city = self.cities[random.randint(0, len(self.cities))]
            street = self.streets[random.randint(0, len(self.streets))]
            house = f"д. {random.randint(0,99)}"
            address = ", ".join([city, street, house])

            phone_number = f"89{random.randint(10,99)}" \
                f"{random.randint(100,999)}" \
                f"{random.randint(10,99)}" \
                f"{random.randint(10,99)}"

            drivers.append(
                {
                    "driver_license": driver_license,
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


if __name__ == "main":
    gen = Generator()

    for car in gen.generate_cars():
        gen.db.cars.insert()

    for driver in gen.generate_drivers():
        gen.db.drivers.insert(
            on_duplicate="update",
            license_number=driver.get("license_number"),
            full_name=driver.get("full_name"),
            address=driver.get("address"),
            phone_number=driver.get("phone_number")
        )

    for fine in gen.generate_fine():
        gen.db.fine.insert()

    for violation in gen.generate_violations():
        gen.db.violations.insert()

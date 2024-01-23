from data import DataBase
from datetime import datetime

database = DataBase()

registration_number = str(input("Введите номер автомобиля: "))
brand = str(input("Марка: "))
model = str(input("Модель: "))
color = str(input("Цвет: "))
manufactured_year = 2000
registration_date = str(datetime.now().date())
owner_license = str(input("Введите лицензию водителя: "))

database.cars.insert(
    registration_number=registration_number,
    brand=brand,
    model=model,
    color=color,
    manufactured_year=manufactured_year,
    registration_date=registration_date,
    owner_license=owner_license
)
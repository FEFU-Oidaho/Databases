from data import DataBase
from datetime import datetime
from random import randint

database = DataBase()

# Блок считывания данных
violation_code = str(input("Введите код нарушения: "))
driver_license = str(input("Введите лицензию нарушевшего: "))

# Автоматически определяемые данные
date = str(datetime.now().date())
time = str(datetime.now().time())

# Статичные данные для теста
inspector_number = 157781
area = "Где-то на улице"
payment_state = 0
payment_size = randint(10000, 25000)
deprivation_size = 0

database.fine.insert(
    violation_code=violation_code,
    driver_license=driver_license,
    inspector_number=inspector_number,
    date=date,
    time=time,
    area=area,
    payment_state=payment_state,
    payment_size=payment_size,
    deprivation_size=deprivation_size
)
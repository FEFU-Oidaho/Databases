from data import DataBase

database = DataBase()

license_number = str(input("Введите номер лицензии: "))
full_name = str(input("Введите полное ФИО: "))
address = str(input("Введите адрес проживагия: "))
phone_number = str(input("Введите номер телефона: "))

database.drivers.insert(
    license_number=license_number,
    full_name=full_name,
    address=address,
    phone_number=phone_number
)
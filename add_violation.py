from data import DataBase

database = DataBase()

# Блок считывания данных
violation_code = str(input("Введите код нарушения: "))
violation_type = str(input("Введите тип: "))

warn_possibility = 0
payment_diapason = "10000 - 25000"
deprivation_diapason = "0 - 12"

database.violations.insert(
    code=violation_code,
    type=violation_type,
    warn_possibility=warn_possibility,
    payment_diapason=payment_diapason,
    deprivation_diapason=deprivation_diapason
)
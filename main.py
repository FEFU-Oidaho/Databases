"""
Main code file
"""
from flask import (
    Flask,
    render_template,
    abort,
    redirect,
    url_for,
    request
)
from data import DataBase
from datetime import datetime
from random import randint


app = Flask(__name__)

database = DataBase()

payload = {}

login_menu = [
    {"name": "Водитель", "url": "/login/driver"},
    {"name": "Инспектор", "url": "/login/inspector"},
    {"name": "Администратор", "url": "/login/administrator"},
]

# Блок перенапрапвления недоступных ссылок на домакшнюю страницу ------------------


@app.route("/")
def closed_main():
    return redirect(url_for("show_homepage"))


@app.route("/login")
def closed_login():
    return redirect(url_for("show_homepage"))


@app.route("/role")
def closed_role():
    return redirect(url_for("show_homepage"))


@app.route("/home")
def show_homepage():
    main_path = "home.html"
    return render_template(
        main_path,
        menu=login_menu
    )


# Пути логина для каждой из программ ----------------------------------------------
@app.route("/login/<login_role>", methods=['GET', 'POST'])
def role_seelctor_login(login_role):

    pages = [
        ("driver", "d_login.html"),
        ("inspector", "i_login.html"),
        ("administrator", "a_login.html")
    ]

    for page, page_path in pages:
        if login_role == page:
            return render_template(
                page_path,
                menu=login_menu
            )

    abort(404)


# Обработка POST запроса для каждого логина ---------------------------------------
@app.post("/login/driver")
def handle_driver_login():
    driver = request.form["license_number"]

    try:
        license_number = int(driver)

    except ValueError:
        abort(404)

    drivers = database.drivers.select(license_number=license_number)
    if drivers:
        global payload

        driver_cars = database.cars.select(owner_license=license_number)
        driver_fines = database.fine.select(driver_license=license_number)

        cars = []
        fines = []

        for car in driver_cars:
            cars.append(
                {
                    "registration_number": car[0],
                    "car_brand": car[1],
                    "car_model": car[2],
                    "car_color": car[3],
                    "manufactured_year": car[4],
                    "registration_date": car[5],
                    "owner_license": car[6],
                }
            )

        for fine in driver_fines:
            fines.append(
                {
                    "id": fine[0],
                    "violation_code": fine[1],
                    "driver_license": fine[2],
                    "inspector_number": fine[3],
                    "date": fine[4],
                    "time": fine[5],
                    "area": fine[6],
                    "payment_state": "Оплачено" if fine[7] else "Не оплачено",
                    "payment_size": fine[8],
                    "deprivation_size": fine[9],
                }
            )

        payload = {
            "last_login_data": drivers[0][0],
            "driver_name": drivers[0][1],
            "driver_address": drivers[0][2],
            "driver_phone": drivers[0][3],
            "driver_cars": cars,
            "driver_fines": fines,
        }

        return redirect("/role/driver")

    abort(404)


@app.post("/login/inspector")
def handle_inspector_login():
    inspector = request.form["inspector_number"]

    try:
        inspector_number = int(inspector)

    except ValueError:
        abort(404)

    if inspector_number:
        global payload

        all_fines = database.fine.select()

        fines = []

        for fine in all_fines:
            fines.append(
                {
                    "id": fine[0],
                    "violation_code": fine[1],
                    "driver_license": fine[2],
                    "inspector_number": fine[3],
                    "date": fine[4],
                    "time": fine[5],
                    "area": fine[6],
                    "payment_state": "Оплачено" if fine[7] else "Не оплачено",
                    "payment_size": fine[8],
                    "deprivation_size": fine[9],
                }
            )

        payload = {
            "last_login_data": inspector_number,
            "all_fines": fines,
        }

        return redirect("/role/inspector")

    abort(404)


@app.post("/login/administrator")
def handle_administrator_login():
    administrator = request.form["administrator_id"]

    try:
        administrator_id = int(administrator)

    except ValueError:
        abort(404)

    if administrator_id:
        global payload

        all_fines = database.fine.select()

        fines = []

        for fine in all_fines:
            fines.append(
                {
                    "id": fine[0],
                    "violation_code": fine[1],
                    "driver_license": fine[2],
                    "inspector_number": fine[3],
                    "date": fine[4],
                    "time": fine[5],
                    "area": fine[6],
                    "payment_state": "Оплачено" if fine[7] else "Не оплачено",
                    "payment_size": fine[8],
                    "deprivation_size": fine[9],
                }
            )

        payload = {
            "last_login_data": administrator_id,
            "all_fines": fines,
        }

        return redirect("/role/administrator")

    abort(404)

# Обработка POST запроса для каждого действия на страницах ------------------------
@app.post("/role/inspector")
def hande_inspector_action():
    violation_code = request.form["add_violation_code"]
    driver_license = request.form["add_violation_driver_license"]

    # Автоматически определяемые данные
    date = str(datetime.now().date())
    time = str(datetime.now().time())

    # Статичные данные для теста
    inspector_number = payload["last_login_data"]
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
    
    return redirect("/role/inspector")

@app.post("/role/administrator")
def hande_administrator_action():
    action = request.form["action"]

    if action == "edit":
        record_id = request.form["edit_violation_id"]
        record_status = request.form["edit_violation_status"]
        database.fine.update({"payment_state": record_status}, id=record_id)
        

    elif action == "delete":
        record_id = request.form["delete_violation_id"]
        database.fine.delete(id=record_id)
    
    return redirect("/role/administrator")
        


# Пути к каждой из программ -------------------------------------------------------
@app.route("/role/<selected_role>", methods=['GET', 'POST'])
def role_seelctor(selected_role):

    pages = [
        ("driver", "driver.html"),
        ("inspector", "inspector.html"),
        ("administrator", "administrator.html")
    ]

    for role, page_path in pages:
        if selected_role == role:
            return render_template(
                page_path,
                menu=login_menu,
                payload=payload
            )

    abort(404)


app.run(
    host="localhost",
    port=8000,
    debug=True
)

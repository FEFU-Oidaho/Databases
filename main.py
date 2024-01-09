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

        payload = {
            "last_login_data": drivers[0][0],
            "driver_name": drivers[0][1],
            "driver_address": drivers[0][2],
            "driver_phone": drivers[0][3],
            "driver_cars": {},
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

        payload = {
            "last_login_data": inspector_number,
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

        payload = {
            "last_login_data": administrator_id,
        }

        return redirect("/role/administrator")

    abort(404)


# Пути к каждой из программ -------------------------------------------------------
@app.route("/role/<selected_role>")
def role_seelctor(selected_role):

    pages = [
        ("driver", "driver.html"),
        ("inspector", "inspector.html"),
        ("administrator", "administrator.html")
    ]

    print(payload)

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

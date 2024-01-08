"""
Main code file
"""
from flask import (
    Flask,
    render_template,
    abort,
    redirect,
    url_for
)


app = Flask(__name__)


login_menu = [
    {"name": "Водитель", "url": "/login/driver"},
    {"name": "Инспектор", "url": "/login/inspector"},
    {"name": "Администратор", "url": "/login/administrator"},
]

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


@app.route("/login/<login_role>")
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


@app.route("/role/<selected_role>")
def role_seelctor(selected_role):

    pages = [
        ("driver", "driver.html"),
        ("inspector", "inspector.html"),
        ("administrator", "aadministrator.html")
    ]

    for role, page_path in pages:
        if selected_role == role:
            return render_template(
                page_path,
                menu=login_menu
            )

    abort(404)

app.run(
    host="localhost",
    port=8000,
    debug=True
)

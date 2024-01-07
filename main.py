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

\
menu = [
    {"name": "Главная", "url": "home"},
    {"name": "Приложение водителя", "url": "driver"},
    {"name": "Приложение инспектора", "url": "inspector"},
    {"name": "Приложение администратора", "url": "administrator"},
]

@app.route("/")
def redirect_to_main():
    return redirect(url_for("show_homepage"))


@app.route("/home")
def show_homepage():
    main_path = "main.html"
    return render_template(
        main_path,
        menu=menu
    )


@app.route("/<selected_role>")
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
                menu=menu
            )

    abort(404)


app.run(
    host="localhost",
    port=8000,
    debug=True
)

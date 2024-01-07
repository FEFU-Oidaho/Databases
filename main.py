"""
Main code file
"""
from flask import (
    Flask,
    render_template
)


app = Flask(__name__)


@app.route("/")
def show_mainpage():
    main_path = "main.html"
    return render_template(main_path)


@app.route("/<selected_role>")
def role_seelctor(selected_role):

    pages = [
        ("driver", "1"),
        ("inspector", "2"),
        ("administrator", "3")
    ]

    for role, page in pages:
        if selected_role == role:
            return page

    return "Not found"


app.run(
    host="localhost",
    port=8000,
    debug=True
)

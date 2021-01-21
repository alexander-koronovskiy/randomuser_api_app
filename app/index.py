import random

from flask import Flask, json, render_template, request
from handler import del_rows, load_rows, show_rows

app = Flask(__name__)


@app.route("/")
def index():
    data = show_rows()
    return render_template(
        "table_overview.html",
        title="Random user by K",
        rows=data,
        user=random.choice(data),
    )


@app.route("/suggestions")
def suggestions():
    text = request.args.get("jsdata")
    suggestions = show_rows()
    suggestions_list = suggestions[: int(text)]
    return render_template("suggestion.html", suggestions=suggestions_list)


@app.route("/user_update")
def user_update():
    data = show_rows()
    return render_template("user.html", user=random.choice(data))


@app.route("/users_info")
def users_info():
    data = show_rows()
    return render_template("users_info.html", users=data)


if __name__ == "__main__":
    del_rows()
    load_rows(rows=10)
    app.run(host="0.0.0.0")

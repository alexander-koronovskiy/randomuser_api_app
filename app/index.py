import random

from flask import Flask, render_template, request
from handler import del_rows, load_rows, show_rows

app = Flask(__name__)


@app.route("/")
def index():
    data = show_rows()
    return render_template(
        "table_overview.html",
        title="Random user by K",
        rows=[random.choice(data) for _ in range(10)],
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


@app.route("/user/<user_id>")
def user_view(user_id):
    data = show_rows()
    user = data[int(user_id)]
    return render_template("user.html", user=user)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    del_rows()
    load_rows(rows=100)
    app.run(host="0.0.0.0")

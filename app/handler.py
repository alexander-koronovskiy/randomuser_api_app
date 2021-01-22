import os
from typing import List

import requests
from peewee import Model, SqliteDatabase, TextField

# db
db = SqliteDatabase("posts.db")


# model
class User(Model):
    first_name = TextField()
    last_name = TextField()
    gender = TextField()
    phone = TextField()
    email = TextField()
    state = TextField()
    img = TextField()

    class Meta:
        database = db


def load_rows(rows: int):
    """
    loading db data when starting app
    """
    data = requests.get(f"https://randomuser.me/api/?results={rows}").json()
    users = []

    for user in data["results"]:
        users.append(
            {
                "first_name": user["name"]["first"],
                "last_name": user["name"]["last"],
                "gender": user["gender"],
                "phone": user["phone"],
                "email": user["email"],
                "state": user["location"]["country"],
                "img": user["picture"]["large"],
            }
        )

    User.create_table()

    with db.atomic():
        query = User.insert_many(users)
        query.execute()


def show_rows() -> List[dict]:
    """
    sending data to client from db
    """
    db.connect()
    users_selected = User.select().order_by(User.id.desc()).dicts().execute()
    row = [user for user in users_selected]
    db.close()
    return row


def del_rows():
    """
    delete old db
    """
    if db:
        os.remove("posts.db")

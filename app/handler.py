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


def initialize_db():
    db.connect()
    db.create_tables([User], safe=True)
    db.close()


def load_rows(rows: int):
    """
    loading db data when starting app
    """
    initialize_db()

    data = requests.get(f"https://randomuser.me/api/?results={rows}").json()
    for user in data["results"]:

        # db data loads
        User.create(
            first_name=user["name"]["first"],
            last_name=user["name"]["last"],
            gender=user["gender"],
            phone=user["phone"],
            email=user["email"],
            state=user["location"]["country"],
            img=user["picture"]["large"],
        ).save()


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

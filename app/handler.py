import os
from typing import List

import requests
from peewee import *
from randomuser import RandomUser

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

    for user in RandomUser.generate_users(rows):

        # gallery loads
        img_file = open(f"static/img/users/{user.get_first_name()}.jpg", "wb")
        img_file.write(requests.get(user.get_picture().format()).content)
        img_file.close()

        # db data loads
        User.create(
            first_name=user.get_first_name(),
            last_name=user.get_last_name(),
            gender=user.get_gender(),
            phone=user.get_phone(),
            email=user.get_email(),
            state=user.get_state(),
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
    delete old information - db and images
    """
    img_dir = "static/img/users/"
    file_list = [f for f in os.listdir(img_dir)]
    for f in file_list:
        os.remove(os.path.join(img_dir, f))
    if db:
        os.remove("posts.db")

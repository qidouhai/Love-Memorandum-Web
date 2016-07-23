# -*- coding: utf-8 -*-
# all the imports
from LoveMemorandum import lm
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
import json


class CurrentUser():

    def __init__(self, username):
        self.username = username

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.username


def getUser(username, password):
    users = json.load(open("./users.json"))
    for user in users:
        if user[0] == username:
            if (password == user[1]):
                print u"成功"
                login_user(CurrentUser(user[0]))
                return True
            else:
                print "没找到"
    print u"没找到，失败"
    return False


def getEmail(username):
    users = json.load(open("./users.json"))
    for user in users:
        if user[0] == username:
            return user[2]
    return None


def initUsers(user1, user2):
    open("./users.json", "w").write(json.dumps([user1, user2], coding="utf-8"))


def getAllUser():
    try:
        users = json.load(open("./users.json"))
        return [a[0] for a in users]
    except:
        return None


@lm.user_loader
def load_user(username):
    users = json.load(open("./users.json"))
    for user in users:
        if user[0] == username:
            return CurrentUser(username)
    return None

# -*- coding: utf-8 -*-
# all the imports

# 邮件
import json
from flask import render_template
from flask_mail import Mail, Message
from LoveMemorandum import app
from threading import Thread
from user import getEmail
mail = Mail(app)


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def readConfig():
    try:
        a = json.load(open('mail.json'))
        app.config['MAIL_SERVER'] = a['MAIL_SERVER']
        app.config['MAIL_PORT'] = a['MAIL_PORT']
        app.config['MAIL_USE_TLS'] = a['MAIL_USE_TLS']
        app.config['MAIL_USE_SSL'] = a['MAIL_USE_SSL']
        app.config['MAIL_USERNAME'] = a['MAIL_USERNAME']
        app.config['MAIL_PASSWORD'] = a['MAIL_PASSWORD']
        app.config['FLASKY_MAIL_SUBJECT_SUFFIX'] = a[
            'FLASKY_MAIL_SUBJECT_SUFFIX']
        app.config['FLASKY_MAIL_SENDER'] = a['FLASKY_MAIL_SENDER']
        return 1
    except:
        return 0


def send_email(a):
    if readConfig():
        email = getEmail(a["sender"])
        msg = Message(app.config['FLASKY_MAIL_SUBJECT_SUFFIX'].format(
            sender=a["sender"]),
            sender=app.config['FLASKY_MAIL_SENDER'],
            recipients=[email])
        msg.html = render_template('mail.html', dict=a)
        # mail.send(msg)
        thr = Thread(target=send_async_email, args=[app, msg])
        thr.start()

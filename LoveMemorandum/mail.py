# -*- coding: utf-8 -*-
# all the imports

# 邮件
from flask import render_template
from flask_mail import Mail, Message
from LoveMemorandum import app
from threading import Thread
from user import getEmail
mail = Mail(app)


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_email(a):
    email = getEmail(a["sender"])
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_SUFFIX'].format(
        sender=a["sender"]),
        sender=app.config['FLASKY_MAIL_SENDER'],
        recipients=[email])
    msg.html = render_template('mail.html', dict=a)
    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()

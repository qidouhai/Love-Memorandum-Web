# -*- coding: utf-8 -*-
# all the imports
# 数据库操作
from LoveMemorandum import app
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug import secure_filename
SQLite = SQLAlchemy(app)


def init_database():
    try:
        Entries.query.all()
    except:
        SQLite.create_all()


class Entries(SQLite.Model):
    __tablename__ = 'entries'
    id = SQLite.Column(SQLite.Integer, primary_key=True, index=True)
    title = SQLite.Column(SQLite.UnicodeText)
    text = SQLite.Column(SQLite.UnicodeText)
    sender = SQLite.Column(SQLite.UnicodeText)
    time = SQLite.Column(SQLite.DateTime)
    url = SQLite.Column(SQLite.UnicodeText, nullable=True)

    def __repr__(self):
        return '<Entry %r>' % self.title

def newEntry(a):
    new_entry = Entries(title=a["title"], text=a["text"],
        sender=a["sender"], time=datetime.utcnow(), url=a["filename"] if "filename" in a else None
        )
    SQLite.session.add(new_entry)
    SQLite.session.commit()
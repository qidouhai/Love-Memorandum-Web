# -*- coding: utf-8 -*-
# all the imports
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    DATABASE = u'./database.db'
    SECRET_KEY = u'Jason & Tiffany'
    UPLOAD_FOLDER = u'./LoveMemorandum/static/userdata/uploads/'
    ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif']
    POSTS_PER_PAGE = 5
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    MAIL_SERVER = '163.177.90.125'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = u'memo@lihanming.me'
    MAIL_PASSWORD = u'ABCabc123'
    FLASKY_MAIL_SUBJECT_SUFFIX = u'{sender} 更新了记事本啦！'
    FLASKY_MAIL_SENDER = u"记事本 <memo@lihanming.me>"
    SQLALCHEMY_DATABASE_URI = u'sqlite:///{path}'.format(
        path=os.path.join(basedir, 'database.db'))

    @staticmethod
    def init_app(app):
        pass
config = {
    'default': Config
}

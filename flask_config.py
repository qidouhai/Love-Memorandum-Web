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
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_DATABASE_URI = u'sqlite:///{path}'.format(
        path=os.path.join(basedir, 'database.db'))

    @staticmethod
    def init_app(app):
        pass
config = {
    'default': Config
}

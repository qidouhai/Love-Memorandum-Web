# -*- coding: utf-8 -*-
from flask import Flask
from flask_config import config
from flask_login import LoginManager
class YourFlask(Flask):
    def create_jinja_environment(self):
        self.config['TEMPLATES_AUTO_RELOAD'] = True
        return Flask.create_jinja_environment(self)
app = YourFlask(__name__)
# app = Flask(__name__)
app.config.from_object(config['default'])
lm = LoginManager(app)
lm.setup_app(app)

import LoveMemorandum.views

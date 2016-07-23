# -*- coding: utf-8 -*-
from flask import Flask
from flask_config import config
from flask_login import LoginManager
app = Flask(__name__)
app.config.from_object(config['default'])
lm = LoginManager(app)
lm.setup_app(app)

import LoveMemorandum.views

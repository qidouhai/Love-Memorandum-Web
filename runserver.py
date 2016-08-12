# -*- coding: utf-8 -*-

from os import environ
from LoveMemorandum import app

if __name__ == '__main__':
    DEBUG = environ.get("SVR_DEBUG", False)
    HOST = environ.get('SVR_HOST', '0.0.0.0')
    PORT = 52766
    # context = ("./cert/test.crt", "./cert/test.key")
    # app.run(HOST, PORT, debug=DEBUG, ssl_context=context)
    app.run(HOST, PORT, debug=DEBUG)

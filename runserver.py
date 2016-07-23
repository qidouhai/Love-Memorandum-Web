"""
This script runs the Management application using a development server.
"""

from os import environ
from LoveMemorandum import app

if __name__ == '__main__':
    DEBUG = environ.get("SVR_DEBUG", False)
    HOST = environ.get('SVR_HOST', '0.0.0.0')
    # try:
    #     PORT = int(environ.get('SVR_PORT', '5555'))
    # except ValueError:
    #     PORT = 5555
    PORT = 52766
    DEBUG = True
    context = ("C:\users\jason\JasonLee.test.crt",
               "C:\users\jason\JasonLee.test.key")
    app.run(HOST, PORT, debug=DEBUG, ssl_context=context)

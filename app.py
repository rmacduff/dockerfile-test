from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy

import os
import socket

app = Flask(__name__)

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

# the values of those depend on your setup
POSTGRES_HOST = get_env_variable("DATABASE_HOST")


@app.route('/')
def test():
    s = socket.socket()
    address = DATABASE_HOST
    port = 5432
    try:
        s.connect((address, port))
        return '<h1>DB Connection: ok</h1>'
    except:
        return '<h1>Something is broken.</h1>'
    finally:
        s.close()
    return "Hello!"


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8080)

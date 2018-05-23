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
DATABASE_HOST = get_env_variable("DATABASE_HOST")
REDIS_HOST = get_env_variable("REDIS_HOST")

def connection_test(name, address, port):
    s = socket.socket()
    try:
        s.connect((address, port))
        return '<h1>{} Connection: ok</h1>'.format(name)
    except:
        return '<h1>{} Connection: failed</h1>'.format(name)
    finally:
        s.close()



@app.route('/')
def test():
    result = ""
    result += connection_test("postgres", DATABASE_HOST, 5432)
    result += connection_test("redis", REDIS_HOST, 6379)
    return result


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8080)

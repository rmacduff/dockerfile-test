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
    s.settimeout(2)
    try:
        #s.connect((address, port), timeout=10000)
        s.connect((address, port))
        return '<h1>{} connection: ok</h1>'.format(name)
    except:
        return '<h1>{} connection: failed</h1>'.format(name)
    finally:
        s.close()



@app.route('/')
def test():
    result = ""
    result += connection_test("postgres", DATABASE_HOST, 5432)
    result += connection_test("redis", REDIS_HOST, 6379)
    result += connection_test("app_be", "127.0.0.1", 9090)
    result += connection_test("Fail check", "10.255.255.1", 9999)
    return result


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8080)

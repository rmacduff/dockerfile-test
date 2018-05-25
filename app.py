from flask import Flask
from flask import render_template

import os
import socket

app = Flask(__name__)

def get_env_variable(name):
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

def connection_test(name, address, port):
    s = socket.socket()
    s.settimeout(2)
    try:
        s.connect((address, port))
        return '{} connection: ok'.format(name)
    except:
        return '{} connection: failed'.format(name)
    finally:
        s.close()



@app.route('/')
def test():
    result = ""
    result += "{}<br>".format(connection_test("postgres", get_env_variable("DATABASE_HOST"), 5432))
    result += "{}<br>".format(connection_test("redis", get_env_variable("REDIS_HOST"), 6379))
    result += "{}<br>".format(connection_test("app_be", "127.0.0.1", 9090))
    #result += "{}<br>".format("DATABASE_PASSWORD: {}".format(get_env_variable("DATABASE_PASSWORD")))
    return result


if __name__ == '__main__':
    app.run(threaded=True,host='0.0.0.0',port=8080)

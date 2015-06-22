# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask import Flask
app = Flask(__name__)

@app.route("/hola/<string:elephants>/<int:a>/<int:b>")
def hello(elephants, a, b):
    user = {
        "first_name": elephants,
        "last_name": "Chebib",
        "sum": a + b
    }
    return "Hello {first_name} {last_name}. <br /> {sum} ☺".format(**user)

if __name__ == "__main__":
    app.static_folder = '../static'
    app.static_url_path = 'static'
    app.debug = True
    app.run()

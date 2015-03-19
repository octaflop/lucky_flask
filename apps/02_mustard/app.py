# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    ctx = {}
    template_name = "home.html"
    return render_template(template_name, ctx=ctx)

if __name__ == "__main__":
    app.static_folder = '../static'
    app.static_url_path = 'static'
    app.debug = True
    app.run()

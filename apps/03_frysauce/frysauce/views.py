# -*- coding: utf-8 -*-

from frysauce import app
from flask import render_template

@app.route("/")
def home():
    users = [
        {
            'first_name': "Faris",
            'last_name': "Chebib"
        }
    ]

    template_name = "home.html"
    return render_template(template_name, users=users)

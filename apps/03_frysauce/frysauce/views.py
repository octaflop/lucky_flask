# -*- coding: utf-8 -*-

from frysauce import app
from flask import render_template

@app.route("/users/")
def home():
    template_name = "home.html"
    return render_template(template_name, users=users)

@app.route("/users/create", methods=['GET', 'POST'])
def create_user_form():
    """
    Displays a form for creating a user
    """
    template_name = "create_user.html"
    users = []

    return render_template(template_name, users=users)


@app.route("/users/<int:id>")
def user_detail():
    return

@app.route("/api/users/<int:id>")
def user_api_list():
    return

@app.route("/api/users/<int:id>")
def user_api_detail():
    return

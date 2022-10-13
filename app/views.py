# app/views.py
from app import app
from flask_mysqldb import MySQL
from flask import render_template

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/articles')
def articles():
    cur = mysql.connection.cursor()
    return render_template("articles.html")
    
from flask import Blueprint, render_template, redirect, session, request, url_for
from . import settings
import sqlite3 as sql

home_bp = Blueprint(
    "home_route", __name__,
    template_folder='templates',
    static_folder='static'
)

@home_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method=="POST":
        admin = request.form.get("username")
        password = request.form.get("password")
        if settings.ADMIN == admin and settings.PASSWORD == password:
            session['user'] = admin
            return redirect(url_for('home_route.home'))
    return render_template("login.html")

@home_bp.route('/home/')
def home():
    if 'user' not in session:
        return redirect(url_for('home_route.login'))
    conn = sql.connect(settings.DB_PATH)
    conn.row_factory = sql.Row
    cursor = conn.cursor()
    
    user_details = cursor.execute("SELECT * FROM user_finding").fetchall()
    print(user_details)
    cursor.close()
    conn.close()
    
    return render_template("index.html", user_details=user_details)

@home_bp.route('/home/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('home_route.login'))
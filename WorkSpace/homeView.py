from flask import Blueprint, render_template 
from flask_login import login_required, current_user

homeView = Blueprint ('homeView', __name__)
@homeView.route('/')
def home():
    return render_template("home.html")

@homeView.route('/mainhome')
@login_required
def mainhome():
    return render_template("mainhome.html")

@homeView.route('/barbering')
@login_required
def barbering():
    return render_template("barbering.html")

@homeView.route('/cleaning')
@login_required
def cleaning():
    return render_template("cleaning.html")

@homeView.route('/carwash')
@login_required
def carwash():
    return render_template("carwash.html")

@homeView.route('/decoration')
@login_required
def decoration():
    return render_template("decoration.html")
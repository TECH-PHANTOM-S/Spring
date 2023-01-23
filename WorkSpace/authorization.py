#from crypt import methods
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint ('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in Successfully!', category = 'success')
                login_user(user, remember = True)
                return redirect(url_for('homeView.mainhome'))
            else:
                flash('Incorrect Password, try again.', category = 'error')
        else:
            flash('Email does not exist.', category = 'error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def signout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods = ['GET', 'POST'])
def usersignup():
    if request.method == 'POST':
        email = request.form.get('email')
        full_name = request.form.get('fullName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must contain more than 3 characters.', category = 'error')
        elif len(full_name) < 3:
            flash('Your full name must contain more than 2 characters.', category ='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category = 'error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category = 'error')
        else:
            new_user = User(email=email, full_name=full_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category = 'success')
            return redirect(url_for('auth.login'))

    return render_template("signup.html", user=current_user)
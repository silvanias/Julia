from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from juliaapp.extensions.database import db, CRUDMixin

blueprint = Blueprint('routes', __name__)

sets = ['julia', 'mandelbrot']

@blueprint.route('/')
def landing():
    return render_template('landing.html')

@blueprint.get('/login')
def get_login():
    return render_template('auth/login.html')

@blueprint.post('/login')
def post_login():
    print(request.form)
    email = request.form.get('email')
    password = request.form.get('password')

    if email == "admin@admin" and password == "password":
        flash('Logged in kinda', category='success')
        return redirect(url_for('routes.profile' , username='admin'))
    return render_template('auth/login.html')

@blueprint.get('/signup')
def get_signup(): 
    return render_template('auth/signup.html')

@blueprint.post('/signup')
def post_signup(): 
    try:
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        if password1 != password2:
            raise Exception('Passwords must match')
        elif len(password1) < 5:
            raise Exception('Passwords must be 5 or more characters')
        elif User.query.filter_by(username=username).first():
            raise Exception('Username is taken')
        elif User.query.filter_by(email=email).first():
            raise Exception('Email already exists')
        
        new_user = User(email = email, username = username, password = generate_password_hash(password1, method = 'pbkdf2:sha256'))
        new_user.save()
        flash('User Created!', category='success')
        return redirect(url_for('routes.profile' , username=username))
    
    except Exception as error_message:
        error = error_message or 'An unkown error occurred while creating a user. Contact me on github :)'
        flash(error, category='error')
        return render_template('auth/signup.html')

@blueprint.get('/logout')
def logout():
    return 'User logged out'

@blueprint.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    all_users = User.query.filter_by(username=username).first()
    return render_template('profile.html', user=user)

@blueprint.route('/gen', methods=['GET', 'POST'])
def gen():
    all_users = User.query.all()
    return render_template('gen.html', users=all_users, sets=sets)
from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from juliaapp.extensions.database import db, CRUDMixin
from flask_login import login_user, login_required, logout_user
# Investigate what all these do
from juliaapp.scripts.mplmandelbrot import pltrender 
from io import BytesIO
from flask import send_file
import matplotlib
matplotlib.use('agg')
import matplotlib.pyplot as plt
import random


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
    try:
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()

        if not user:
            raise Exception('No user with the given email exists')
        elif not check_password_hash(user.password, password=password):
            # max limit?
            raise Exception('Password incorrect')
        
        login_user(user)
        flash(f'{user.username} logged in :D', category='success')
        return redirect(url_for('routes.profile' , username=user.username))
    
    except Exception as error_message:
        error = error_message or 'An error occurred while loggin in. Contact me on GitHub :)'
        flash(error_message, category='error')
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
        login_user(new_user)
        flash('User Created!', category='success')
        return redirect(url_for('routes.profile' , username=username))
    
    except Exception as error_message:
        error = error_message or 'An unkown error occurred while creating a user. Contact me on github :)'
        flash(error, category='error')
        return render_template('auth/signup.html')

@blueprint.get('/logout')
def logout():
    logout_user()
    return redirect(url_for('routes.get_login'))

@blueprint.route('/profile/<username>')
@login_required
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    all_users = User.query.filter_by(username=username).first()
    return render_template('profile.html', user=user)

@blueprint.get('/gen')
def get_gen():
    return render_template('gen.html', sets=sets)

@blueprint.post('/gen')
def post_gen():
    try:
        # TODO: dont allow empty form (add checks)  
        realnum = request.form.get('realnum')
        imagnum = request.form.get('imagnum')
        chosenSet = request.form.get('sets')
        print(chosenSet,imagnum,realnum)
        flash('Form submitted', category='success')
        return render_template('gen.html', sets=sets)

    except Exception as error_message:
        error = error_message or 'An unkown error occurred. Contact me on github :)'
        flash(error, category='error')
        return render_template('gen.html', sets=sets)
    

@blueprint.route('/plot_gen')
def plot_gen():
    return render_template('plot_gen.html')

@blueprint.route('/mandelbrot.png')
def mandelbrot():
    #DO NOT DELETE UNUSED VARIABLE HERE
    fig, ax = plt.subplots()
    pltrender()
    return nocache(fig_response(fig))

def fig_response(fig):
    """Turn a matplotlib Figure into Flask response"""
    img_bytes = BytesIO()
    fig.savefig(img_bytes)
    img_bytes.seek(0)
    return send_file(img_bytes, mimetype='image/png')

def nocache(response):
    """Add Cache-Control headers to disable caching a response"""
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response

"""
    try:
        fig = pltrender()
        output = io.BytesIO()
        FigureCanvas(fig).print_png(output)
        return Response(output.getvalue(), mimetype='image/png')

    except Exception as error_message:
        error = error_message or 'An unkown error occurred while creating a user. Contact me on github :)'
        flash(error, category='error')
        return render_template('gen.html', sets=sets)
"""
    
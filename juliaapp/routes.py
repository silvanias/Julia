from flask import Blueprint, render_template, redirect, url_for, request, flash
from .models import User
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
    email = request.form.get('email')
    username = request.form.get('username')
    password1 = request.form.get('password1')
    password2 = request.form.get('password2')
    if password1 != password2:
        flash('Passwords must match', category='error')
    elif len(password1) < 5:
        flash('Passwords must be 5 or more characters', category='error')
    else:
        new_user = User(email = email, username = username, password = password1)
        new_user.save()
        flash('User Created!', category='success')
        return redirect(url_for('routes.profile' , username=username))
    return render_template('auth/signup.html')

@blueprint.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username=username).first_or_404()
    all_users = User.query.filter_by(username=username).first()
    return render_template('profile.html', user=user)

@blueprint.route('/gen', methods=['GET', 'POST'])
def gen():
    all_users = User.query.all()
    return render_template('gen.html', users=all_users, sets=sets)
from flask import Blueprint, render_template, redirect, url_for, request
from .models import User

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
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email == "admin@admin" and password == "password":
            print("logged in")
            return redirect(url_for('routes.gen'))
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
        print("Passwords must match")
    elif len(password1) < 5:
        print('Passwords must be 5 or more characters')
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
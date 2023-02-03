from flask import Blueprint, render_template, redirect, url_for, request

blueprint = Blueprint('routes', __name__)

@blueprint.route('/')
def landing():
    return render_template('landing.html')

@blueprint.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        if email == "admin@admin" and password == "password":
            print("logged in")
            return redirect(url_for('routes.gen'))
    return render_template('auth/login.html')

@blueprint.route('/signup')
def signup():
    return render_template('auth/signup.html')

@blueprint.route('/gen')
def gen():
    return render_template('gen.html')
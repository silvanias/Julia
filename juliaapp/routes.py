from flask import Blueprint, render_template, redirect, url_for

blueprint = Blueprint('routes', __name__)

@blueprint.route('/')
def landing():
    return render_template('landing.html')

@blueprint.route('/login')
def login():
    return render_template('auth/login.html')

@blueprint.route('/signup')
def signup():
    return render_template('auth/signup.html')

@blueprint.route('/gen')
def gen():
    return render_template('gen.html')
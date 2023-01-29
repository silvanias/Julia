from flask import Blueprint, render_template, redirect, url_for

blueprint = Blueprint('routes', __name__)

@blueprint.route('/')
def landing():
    return render_template('landing.html')

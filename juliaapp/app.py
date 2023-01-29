from flask import Flask, url_for, render_template

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('instance.config')

@app.route('/')
def landing():
    return render_template('landing.html')

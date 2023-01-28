from flask import Flask

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('instance.config')

@app.route('/')
def landing():
    return 'Wassup Earth'

if __name__ == '__main__':
  app.run()
# If encountering unauthorised errors: chrome://net-internals/#sockets -> [Flush socket pools]
from juliaapp.app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
from __init__ import create_app
from waitress import serve

app = create_app()

if __name__ == "__main__":
    serve(app, host="localhost", port=8000)
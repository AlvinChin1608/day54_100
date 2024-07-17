# A minimal flash application
from flask import Flask

app = Flask(__name__)

"""The @app.route("/") is called Python Decorator
Basically, functions that would give additional functionalities to a function

Head over to the explain_file.py for better explanation"""

@app.route("/")
def hello():
    return "Hello, World!"

# if somebody goes to the URL /bye, this trigger
@app.route("/bye")
def say_bye():
    return "bye"

"""Some thing but we don't to type the export FLASK_APP=hello.py
and the flask run in terminal to start the server and manually end it using ctrl+c"""
if __name__ =="__main__":
    app.run()



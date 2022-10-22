#Import Flask
from flask import Flask
# Create an app, being sure to pass __name__
app = Flask(__name__)
@app.route('/')
@app.route('/')
def hello_world():
    return 'Hello world'

# export FLASK_APP=app.py

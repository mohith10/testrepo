from flask import Flask
from flask import json
from flask import request

app = Flask(__name__)




@app.route("/",methods = ['POST','GET'])
def home_page():
    return '<h1>Hello World</h1>'



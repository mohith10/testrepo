from flask import Flask
from flask import json
from flask import request
from webexteamssdk import WebexTeamsAPI

app = Flask(__name__)




@app.route("/",methods = ['POST','GET'])
def home_page():
    return 'hello world hehe'

if __name__ == '__main__':
    app.run(debug=True)
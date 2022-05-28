from flask import Flask,render_template,request,jsonify
from selenium import webdriver
import os,signal
import Gesture_Controller
from werkzeug.serving import make_server
app1 = Flask(__name__)
@app1.route('/')
def index():
    return render_template('index.html')

@app1.route("/start/", methods=['POST'])
def move_forward():
        x=Gesture_Controller.GestureController()
        x.start()
        return render_template('index.html')


@app1.route('/shut/')
def stopServer():
    x=Gesture_Controller.GestureController()
    x.end()
    return render_template('index.html')
if __name__ == "__main__":
    app1.run(debug=True)
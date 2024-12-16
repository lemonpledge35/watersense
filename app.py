import numpy as np
from flask import Flask, render_template, request
import datetime
import time
from read import read_pin
import glob



app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def home():
    value = read_pin(11)
    print(value)
    if value == 1:
        text = False
    elif value == 0:
        text = True
    if request.method == 'GET':
        return render_template('home.html',value = text)
    


@app.route("/test/")
def test():
    return render_template('test.html')

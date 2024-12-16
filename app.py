import numpy as np
from flask import Flask, render_template, request
import datetime
import time
from read import reand_pin
import glob



app = Flask(__name__)

@app.route("/", methods = ['GET','POST'])
def home():
    value = read(11)
    if value == 1:
        text = "false"
    elif value == 0:
        text = 'true'
    if request.method == 'GET':
        return render_template('home.html',value = text)
    


@app.route("/test/")
def test():
    return render_template('test.html')

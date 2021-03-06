from flask import Flask, render_template, redirect, url_for, request
from utils import UTILS

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('slam_book.html')

@app.route('/submit',methods = ['POST'])
def submit():
    result = request.form
    #dict = []
    dict2 = {}
    for k,v in result.items():
        #dict.append([f"{k}:{v}"])
        dict2[k] = v
    print('\n', dict2)
    u = UTILS(username=dict2['YourName'], data=dict2, app=app)
    u.run()
    return redirect(url_for('index'))

from flask import Flask, render_template, redirect, url_for, request, jsonify
from utils import UTILS
import json

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('slam_book.html')

@app.route('/submit',methods = ['POST'])
def submit():
    result = request.form
    dict = []
    for k,v in result.items():
        dict.append([f"{k}:{v}"])
    print(dict, '\n')
    u = UTILS(username=dict[0][1], data=dict)
    u.run()
    return redirect(url_for('index'))

#if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
#    app.run(threaded=True, port=5000, debug=True)
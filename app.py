from flask import Flask, render_template, redirect, url_for, request
from utils import UTILS

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('slam_book.html')

@app.route('/submit',methods = ['POST'])
def submit():
    result = request.form
    dict = []
    #dict2 = {}
    for k,v in result.items():
        dict.append([f"{k}:{v}"])
        #dict2[k] = v
    #print(dict, '\n', dict2)
    u = UTILS(username=dict[0][0].split(':')[-1], data=str(dict), app=app)
    #u = UTILS(username=dict2['YourName'], data=dict2, app=app)
    u.run()
    return redirect(url_for('index'))

#if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    #app.run(threaded=True, port=5000, debug=True)
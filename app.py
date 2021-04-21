from flask import Flask, render_template, redirect, url_for, request
from utils import UTILS

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('slam_book.html')

@app.route('/submit',methods = ['POST'])
def submit():
   if request.method == 'POST':
      result = request.form
      dict = {}
      for k,v in result.items():
          dict[k] = v
      u = UTILS(data=dict)
      u.run()
      return redirect(url_for('index'))
   return redirect(url_for('index'))

#if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
#    app.run(threaded=True, port=5000)
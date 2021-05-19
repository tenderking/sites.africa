from sites import app
from flask import render_template

@app.route('/')
def index():
    #return "Hello World"
     return render_template('index.html')
from flask import Flask, app, render_template

app = Flask(__name__)

#Routes
from user import routes

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')
    
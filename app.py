from flask import Flask, app, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/dashboard/')
def dashboard():
    return render_template('dashboard.html')
    
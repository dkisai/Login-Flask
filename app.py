from flask import Flask, app, render_template, request, redirect, url_for, flash, jsonify


app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
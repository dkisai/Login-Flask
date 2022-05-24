from flask import Flask
from app import app
from user.models import User

@app.route('/users/signup/', methods=['GET'])
def signup():
    user = User()
    return user.singup()
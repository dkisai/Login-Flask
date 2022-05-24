from flask import Flask, jsonify

class User:

        def singup(self):

            user = {
                '_id': '',
                'username': '',
                'password': '',
                'email': '',
                'firstname': '',
                'lastname': ''
            }
            return jsonify(user), 200
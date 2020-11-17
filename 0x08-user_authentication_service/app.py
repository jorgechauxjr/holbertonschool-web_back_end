#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """welcome message"""
    return jsonify({"message": "Bienvenue"})

@app.route("/users", methods=['POST'], strict_slashes=False)
def register_user() -> str:
    """POST /users
    JSON body:
        - email
        - password
    Return:
        - JSON payload
    """
    email = request.form.get("email")
    pwd = request.form.get("password")
    try:
        AUTH.register_user(email, pwd)
        return jsonify({"email": email, "message": "user created"})
    except Exception:
        return jsonify({"message": "email already registered"}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

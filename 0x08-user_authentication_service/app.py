#!/usr/bin/env python3
"""
Basic Flask app
"""
from flask import Flask
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def welcome() -> str:
    """welcome message"""
    return jsonify({"message": "Bienvenue"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
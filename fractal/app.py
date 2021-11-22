#!/usr/bin/env python3
""" Fractal generation demo. Copyright (C) 2021 Evan Beeton. """
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, world!</p>"

if __name__ == '__main__':
    app.logger.setLevel("INFO")
    app.run(debug=False, host='0.0.0.0')

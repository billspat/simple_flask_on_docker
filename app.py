#!/usr/bin/env python
# coding: utf-8
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def index(message="hello from Flask"):
    return render_template('index.jinja2', message=message)

if __name__ == '__main__':
    app.run()

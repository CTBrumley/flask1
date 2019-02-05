# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 13:44:48 2019

@author: todd
"""


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World"

app.run(port=5000)








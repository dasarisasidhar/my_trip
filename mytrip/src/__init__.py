"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

from mytrip.src import controller

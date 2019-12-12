"""
The flask application package.
"""

from flask import Flask
app = Flask(__name__)

import mytrip.src.controller.pilot_views
import mytrip.src.controller.user_views
import mytrip.src.controller.views



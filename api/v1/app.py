#!/usr/bin/python3
"""
Main file for the API
"""

from flask import Flask, jsonify
from models import storage
from api.v1.views import app_views
import os
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(app_views)
cors = CORS(app, resources={"/*": {"origins": "0.0.0.0"}})


@app.teardown_appcontext
def teardown_db(exception):
    """
    Closes the database
    """
    storage.close()


@app.errorhandler(404)
def not_found_error(error):
    """Returns a JSON-formatted 404 status code response"""
    res = jsonify({"error": "Not found"})
    res.status_code = 404
    return res


if __name__ == '__main__':
    app.run(
        host=os.getenv("HBNB_API_HOST", "0.0.0.0"),
        port=os.getenv("HBNB_API_PORT", "5000"),
        threaded=True
    )

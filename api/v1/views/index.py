#!/usr/bin/python3
"""
Returns json status response
"""

from flask import jsonify
from api.v1.views import app_views


@app_views.route('/status', methods=['GET'])
def status():
    """Returns status"""
    return jsonify({"status": "OK"})

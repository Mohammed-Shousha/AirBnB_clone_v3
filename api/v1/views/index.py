#!/usr/bin/python3
"""
returns json status response
"""

from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', methods=['GET'])
def status():
    """
    function for status route that returns the status
    """
    if request.method == 'GET':
        res = {"status": "OK"}
        return jsonify(res)


@app_views.route('/stats', methods=['GET'])
def stats():
    """
    function for status route that returns the status
    """
    if request.method == 'GET':
        res = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
        }
        return jsonify(res)

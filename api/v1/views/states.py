#!/usr/bin/python3
"""State view module"""

from api.v1.views import app_views
from flask import abort, jsonify, request, make_response
from models import storage
from models.state import State


@app_views.route('/states', methods=['GET'], strict_slashes=False)
def get_states():
    """Retrieves the list of all State objects"""
    states = [state.to_dict() for state in storage.all("State").values()]

    return jsonify(states)


@app_views.route('/states/<string:state_id>', methods=['GET'],
                 strict_slashes=False)
def get_state(state_id):
    """Retrieves a State object based on its state_id"""
    state = storage.get("State", state_id)

    if state is None:
        abort(404)

    return jsonify(state.to_dict())


@app_views.route('/states/<string:state_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_state(state_id):
    """Deletes a State object based on its state_id"""
    state = storage.get("State", state_id)

    if state is None:
        abort(404)

    state.delete()
    storage.save()

    return (jsonify({}))


@app_views.route('/states/', methods=['POST'], strict_slashes=False)
def post_state():
    """Creates a State"""
    data = request.get_json()

    if not data:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)

    if 'name' not in data:
        return make_response(jsonify({'error': 'Missing name'}), 400)

    state = State(**data)
    state.save()

    return make_response(jsonify(state.to_dict()), 201)


@app_views.route('/states/<string:state_id>', methods=['PUT'],
                 strict_slashes=False)
def put_state(state_id):
    """Updates a State object based on its state_id"""
    state = storage.get("State", state_id)

    if state is None:
        abort(404)

    data = request.get_json()

    if not data:
        return make_response(jsonify({'error': 'Not a JSON'}), 400)

    for attr, val in data.items():
        if attr not in ['id', 'created_at', 'updated_at']:
            setattr(state, attr, val)

    state.save()

    return jsonify(state.to_dict())

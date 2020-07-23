import json
import os
import traceback
from datetime import datetime

from flask import Blueprint, request, current_app, jsonify
from werkzeug.exceptions import abort

terra_controller = Blueprint('terra_controller', __name__)

@terra_controller.route('/terra/general', methods=['GET'])
def get_data_general():
    try:
        date_string = request.args.get('date')
        date = datetime.strptime(date_string, '%Y-%m-%d')
    except Exception:
        traceback.print_exc()
        abort(400, 'argument \'date\' is wrong, format: %Y-%m-%d')
        return

    file_path = os.path.join(current_app.config['TERRA_PATH_GENERAL'], date_string + '.json')

    if not os.path.isfile(file_path):
        abort(404, 'data not found')

    with open(file_path, 'r') as file:
        return jsonify(json.load(file))


@terra_controller.route('/terra/payments', methods=['GET'])
def get_data_payments():
    try:
        date_string = request.args.get('date')
        date = datetime.strptime(date_string, '%Y-%m-%d')
    except Exception:
        traceback.print_exc()
        abort(400, 'argument \'date\' is wrong, format: %Y-%m-%d')
        return

    file_path = os.path.join(current_app.config['TERRA_PATH_PAYMENTS'], date_string + '.json')

    if not os.path.isfile(file_path):
        abort(404, 'data not found')

    with open(file_path, 'r') as file:
        return jsonify(json.load(file))


@terra_controller.route('/terra/transactions', methods=['GET'])
def get_data_transactions():
    try:
        date_string = request.args.get('date')
        date = datetime.strptime(date_string, '%Y-%m-%d')
    except Exception:
        traceback.print_exc()
        abort(400, 'argument \'date\' is wrong, format: %Y-%m-%d')
        return

    file_path = os.path.join(current_app.config['TERRA_PATH_TRANSACTIONS'], date_string + '.json')

    if not os.path.isfile(file_path):
        abort(404, 'data not found')

    with open(file_path, 'r') as file:
        return jsonify(json.load(file))


@terra_controller.route('/terra/user', methods=['GET'])
def get_data_user():
    try:
        date_string = request.args.get('date')
        date = datetime.strptime(date_string, '%Y-%m-%d')
    except Exception:
        traceback.print_exc()
        abort(400, 'argument \'date\' is wrong, format: %Y-%m-%d')
        return

    file_path = os.path.join(current_app.config['TERRA_PATH_USER'], date_string + '.json')

    if not os.path.isfile(file_path):
        abort(404, 'data not found')

    with open(file_path, 'r') as file:
        return jsonify(json.load(file))

@terra_controller.route('/terra/rolling_retention', methods=['GET'])
def get_data_rolling_retention():
    try:
        date_string = request.args.get('date')
        date = datetime.strptime(date_string, '%Y-%m-%d')
    except Exception:
        traceback.print_exc()
        abort(400, 'argument \'date\' is wrong, format: %Y-%m-%d')
        return

    file_path = os.path.join(current_app.config['TERRA_PATH_ROLLING_RETENTION'], date_string + '.json')

    if not os.path.isfile(file_path):
        abort(404, 'data not found')

    with open(file_path, 'r') as file:
        return jsonify(json.load(file))
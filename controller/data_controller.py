import os
import traceback
from datetime import datetime

from flask import Blueprint, request, current_app, jsonify
from werkzeug.exceptions import abort

data_controller = Blueprint('data_controller', __name__)

@data_controller.route('/data/<symbol>/realized_market_cap', methods=['GET'])
def get_realized_market_cap(symbol):

    try:
        date = request.args.get('date')
        date = datetime.strptime(date, '%Y-%m-%d')
    except Exception:
        traceback.print_exc()
        abort(400, 'argument \'date\' is wrong, format: %Y-%m-%d')
        return

    date_string = date.strftime('%Y-%m-%d')
    symbol_file = current_app.config['PATH_REALIZED_MARKET_CAP'] + symbol

    if not os.path.exists(symbol_file):
        abort(400, 'symbol not found')

    with open(symbol_file, 'r') as file:

        for line_raw in file:
            line = line_raw.split(',')

            if line[0] == date_string:
                return jsonify({
                    'num_coins': float(line[1]),
                    'not_moved_coins': float(line[2]),
                    'realized_market_cap': float(line[3]),
                    'coins_older_1y': float(line[4]),
                    'num_transactions': float(line[5]),
                    'transaction_volume': float(line[6]),
                    'num_holder': float(line[7]),
                })

    return ''


@data_controller.route('/data/<symbol>/token_holder_stats', methods=['GET'])
def get_token_holder_stats(symbol):

    try:
        date = request.args.get('date')
        date = datetime.strptime(date, '%Y-%m-%d')
    except Exception:
        traceback.print_exc()
        abort(400, 'argument \'date\' is wrong, format: %Y-%m-%d')
        return

    date_string = date.strftime('%Y-%m-%d')
    symbol_file = current_app.config['PATH_TOKEN_HOLDER_STATS'] + symbol

    if not os.path.exists(symbol_file):
        abort(400, 'symbol not found')

    with open(symbol_file, 'r') as file:

        for line_raw in file:
            line = line_raw.split(',')

            if line[0] == date_string:
                return jsonify({
                    'token_contracts_balance': float(line[1]),
                    'team_balance': float(line[2]),
                    'exchanges_balance': float(line[3]),
                    'top20': float(line[4]),
                    'top50': float(line[5]),
                    'top100': float(line[6]),
                    'top200': float(line[7]),
                    'retail': float(line[8]),
                })

    return ''


@data_controller.route('/data/<symbol>/top_token_holder', methods=['GET'])
def get_top_token_holder(symbol):

    try:
        date = request.args.get('date')
        date = datetime.strptime(date, '%Y-%m-%d')
    except Exception:
        traceback.print_exc()
        abort(400, 'argument \'date\' is wrong, format: %Y-%m-%d')
        return

    date_string = date.strftime('%Y-%m-%d')
    symbol_file = current_app.config['PATH_TOP_TOKEN_HOLDER'] + symbol + '/' + date_string

    if not os.path.exists(symbol_file):
        abort(400, 'no data found')

    response = ''
    with open(symbol_file, 'r') as file:

        return ''.join(file.readlines())


@data_controller.route('/data/<symbol>/top_token_holder_normalized', methods=['GET'])
def get_top_token_holder_normalized(symbol):

    try:
        date = request.args.get('date')
        date = datetime.strptime(date, '%Y-%m-%d')
    except Exception:
        traceback.print_exc()
        abort(400, 'argument \'date\' is wrong, format: %Y-%m-%d')
        return

    date_string = date.strftime('%Y-%m-%d')
    symbol_file = current_app.config['PATH_TOP_TOKEN_HOLDER_NORMALIZED'] + symbol + '/' + date_string

    if not os.path.exists(symbol_file):
        abort(400, 'no data found')

    response = ''
    with open(symbol_file, 'r') as file:

        return ''.join(file.readlines())
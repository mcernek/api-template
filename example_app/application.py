from random import randint

from flask import Flask, jsonify, abort, make_response
from webargs import fields
from webargs.flaskparser import use_args, parser

app = Flask(__name__)

app.config['SESSION_COOKIE_SECURE'] = True


@parser.error_handler
def handle_request_parsing_error(err):
    response = make_response(
        jsonify(status='validation_error', errors=err.messages),
        err.status_code
    )
    abort(response)


@app.route('/ping', methods=['GET'])
def ping():
    return jsonify(status='pong')


@app.route('/prediction', methods=['GET'])
@use_args({
    'from': fields.DateTime(location='query', required=True),
    'to': fields.DateTime(location='query', required=True),
})
def prediction(args):
    response = jsonify({
        'status': 'ok',
        'from': args['from'],
        'to': args['to'],
        'sales': {
            'amount': randint(1000, 100000),
            'currency': 'EUR',
        }
    })
    return response, 200

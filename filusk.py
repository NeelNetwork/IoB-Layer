from flask import Flask , request , render_template ,Response , jsonify , abort
import requests
import json
import os
import sys

import ModuleHandler 


app = Flask(__name__)


@app.route('/entry/new',  methods=['POST'])
def NewEntry():
	# print( request.path , request.full_path , request.script_root , request.base_url , request.url  )
	# print( request.url_root , request.endpoint , request.method , request.cookies , request.data )
	# print( request.headers ,  request.args , request.form , request.remote_addr )
	if not request.json or not 'Type' in request.json or not 'WavesAddress' in request.json :
        abort(400)

	Type = request.json['Type']
	WavesAddress = request.json['WavesAddress']

	coin = ModuleHandler.str_to_class('Modules.'+Type, Type)
	res = coin.createWallet(WavesAddress)

	print(res)
	response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
	return response


@app.route('/transaction/check',  methods=['POST'])
def TransactionCheck():
	# print( request.path , request.full_path , request.script_root , request.base_url , request.url  )
	# print( request.url_root , request.endpoint , request.method , request.cookies , request.data )
	# print( request.headers ,  request.args , request.form , request.remote_addr )

	if not request.json or not 'Type' in request.json or not 'WavesAddress' in request.json :
        abort(400)

    Type = request.json['Type']
    WavesAddress = request.json['WavesAddress']

	coin = ModuleHandler.str_to_class('Modules.'+Type, Type)
	res = coin.CheckTransaction(WavesAddress)

	print(res)
	response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
	return response



if __name__ == '__main__':
    app.run(debug=True)
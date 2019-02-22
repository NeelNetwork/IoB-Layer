from flask import Flask , request , render_template ,Response , jsonify , abort
import requests
import json
import os
import sys
import pywaves

import ModuleHandler 

WAVES = pywaves.Address(address="" , privateKey="")
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
	res = coin.CreateWallet(WavesAddress)

	print(res)
	response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
	return response


@app.route('/entry/verify',  methods=['POST'])
def VerifyEntry():
	# print( request.path , request.full_path , request.script_root , request.base_url , request.url  )
	# print( request.url_root , request.endpoint , request.method , request.cookies , request.data )
	# print( request.headers ,  request.args , request.form , request.remote_addr )
	if not request.json or not 'Type' in request.json or not 'WavesAddress' in request.json :
		abort(400)

	Type = request.json['Type']
	WavesAddress = request.json['WavesAddress']
	coin = ModuleHandler.str_to_class('Modules.'+Type, Type)
	res = coin.VerifyWallet(WavesAddress)
	recipient = pywaves.Address(address=WavesAddress)
	BTC = pywaves.Asset('8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS')
    WAVES.sendAsset(recipient,BTC,res)

	print(res)
	response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
	return response




@app.route('/transaction/settle',  methods=['GET'])
def SettleTransaction():
	# print( request.path , request.full_path , request.script_root , request.base_url , request.url  )
	# print( request.url_root , request.endpoint , request.method , request.cookies , request.data )
	# print( request.headers ,  request.args , request.form , request.remote_addr )

	# if not request.json or not 'Type' in request.json or not 'WavesAddress' in request.json :
        # abort(400)

    # Type = request.json['Type']
    # WavesAddress = request.json['WavesAddress']

	coin = ModuleHandler.str_to_class('Modules.'+Type, Type)
	res = coin.SettleTransaction(WavesAddress)

	print(res)
	response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
	return response



if __name__ == '__main__':
    app.run(debug=True)
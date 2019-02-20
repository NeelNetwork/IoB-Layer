from flask import Flask , request , render_template ,Response , jsonify , abort
import requests
import json
import os
import sys

from Modules import *


app = Flask(__name__)

def NewEntry(Type,WavesAdr) :

method_name = 'install' # set by the command line options
my_cls = MyClass()

method = None

try:
    method = getattr(my_cls, method_name)
except AttributeError:
    raise NotImplementedError("Class `{}` does not implement `{}`".format(my_cls.__class__.__name__, method_name))


    
	method_name = 'createWallet' # set by the command line options
	possibles = globals().copy()
	possibles.update(locals())
	method = possibles.get(method_name)
	if not method:
		raise NotImplementedError("Method %s not implemented" % method_name)
	method()

	try:
		pass
	except Exception as e:
		raise e

@app.route('/entry/new',  methods=['POST'])
def WalletCreate():
	print( request.path , request.full_path , request.script_root , request.base_url , request.url  )
	print( request.url_root , request.endpoint , request.method , request.cookies , request.data )
	print( request.headers ,  request.args , request.form , request.remote_addr )

	if not request.json or not 'Type' in request.json or not 'WavesAdr' in request.json :
        abort(400)

    Type = request.json['Type']
    WavesAdr = request.json['WavesAdr']

	res = NewEntry(Type,WavesAdr)

	print(res)
	response = app.response_class(
        response=json.dumps(res),
        status=200,
        mimetype='application/json'
    )
	return response





if __name__ == '__main__':
    app.run(debug=True)
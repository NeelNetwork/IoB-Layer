from bitcoinlib import *


class BTC(object):

    def createWallet(self,WavesAddress):

    	w = wallet_create_or_open(WavesAddress ,encoding='base58' ,network='testnet')
		# print(len(w.get_keys()))
		key = w.get_key(0)
		# print(key.key().dict())
		publkey = bytes.fromhex( key.dict()['key_public'] )
		privkey = bytes.fromhex( key.dict()['key_private'] )
		# print(publkey)
		# print({'key_private': base58.b58encode(privkey) ,'key_public': base58.b58encode(publkey)})
		print(key.address)
		return {'address' : key.address }


	def generateKeys(self,WavesAddress) :

		w = wallet_create_or_open(WavesAddress ,encoding='base58' ,network='testnet')
		# print(len(w.get_keys()))
		key = w.get_key(0)
		# print(key.key().dict())
		publkey = bytes.fromhex( key.dict()['key_public'] )
		privkey = bytes.fromhex( key.dict()['key_private'] )
		# print(publkey)
		print({'key_private': base58.b58encode(privkey) ,'key_public': base58.b58encode(publkey)})
		print(key.address)
		return { 'key_private' : base58.b58encode(privkey) , 'key_public' : base58.b58encode(publkey) }



		# walletList = wallets_list()
  #   	# print(len(l))
		# lnames =[ walletList[i]['name'] for i in range(len(walletList)) ]
		# if wavseAdr in lnames :
		# 	w = HDWallet(wavseAdr)
		# 	print(w.get_key().address)
		# 	return {'address' : w.get_key().address }
		# 	# print({'key_private': w.get_key().dict()['key_private'] ,'key_public': w.get_key().dict()['key_public']})
		# 	# print(w.dict()['key_public'])
		# 	# print(lnames.index(wavseAdr))
		# 	# print(w.info())
		# else : 
		# 	w = HDWallet.create( wavseAdr ,  network='testnet')
		# 	print(w.get_key().address)
		# 	return {'address' : w.get_key().address }

		# 	# print({'key_private': w.get_key().dict()['key_private'] ,'key_public': w.get_key().dict()['key_public']})


		
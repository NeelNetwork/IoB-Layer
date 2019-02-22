# from bitcoinlib import *
from bitmerchant.wallet import Wallet
from blockcypher import create_wallet_from_address,get_address_details,get_wallet_addresses,get_transaction_details



class BTC(object):
	network = 'testnet'
	APIKEY = '17536ffbfb674825838e33b77deeec9f'

    def CreateWallet(self,WavesAddress):

    	newWallet = Wallet.new_random_wallet()
    	# private_key_hex = newWallet.get_private_key_hex()
    	# public_key_hex = newWallet.get_public_key_hex()

    	serializeWlt = newWallet.serialize()
    	newAddress = newWallet.to_address()
		#TODO SAVE WAVESAddress , serializeWlt in DB
		BTCWallet = create_wallet_from_address(wallet_name=WavesAddress, address=newAddress, api_key=APIKEY)

		return {'addresses' : BTCWallet['addresses'][0] }

  		# w = wallet_create_or_open(WavesAddress ,encoding='base58' ,network=self.network)
		# # print(len(w.get_keys()))
		# key = w.get_key(0)
		# # print(key.key().dict())
		# publkey = bytes.fromhex( key.dict()['key_public'] )
		# privkey = bytes.fromhex( key.dict()['key_private'] )
		# # print(publkey)
		# # print({'key_private': base58.b58encode(privkey) ,'key_public': base58.b58encode(publkey)})
		# print(key.address)
		# return {'address' : key.address }



	def VerifyWallet(self,WavesAddress):

		



	def CheckTransaction(self,WavesAddress) :
		serializeWlt = None
		#TODO read serializeWlt from DB
		_wallet = get_wallet_addresses(wallet_name=WavesAddress, api_key=APIKEY)

		details = get_address_details(_wallet['addresses'][0])
		tx_hash = details['txrefs'][0]['tx_hash']
		transaction_details = get_transaction_details(tx_hash)


		return { None }





		# walletList = wallets_list()
     	# print(len(l))
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


		
# from bitcoinlib import *
from bitmerchant.wallet import Wallet
from blockcypher import create_wallet_from_address,get_address_details,get_wallet_addresses,get_transaction_details
import sqlite3 as lite
import pywaves



class BTC(object):
	# network = 'testnet'
	APIKEY = '17536ffbfb674825838e33b77deeec9f'
	WAVES = pywaves.Address(address="" , privateKey="")



	def CreateWallet(self,WavesAddress):

		newWallet = Wallet.new_random_wallet()
		# private_key_hex = newWallet.get_private_key_hex()
		# public_key_hex = newWallet.get_public_key_hex()
		serializedWallet = newWallet.serialize()
		newAddress = newWallet.to_address()

		BTCWallet = create_wallet_from_address(wallet_name=WavesAddress, address=newAddress, api_key=self.APIKEY)
		#TODO SAVE WAVESAddress , serializeWlt in DB
		print(BTCWallet)
		con = lite.connect('test.db')
		with con:
			cur = con.cursor()
			cur.execute("CREATE TABLE IF NOT EXISTS addresses(WavesAddress TEXT , serializedWallet TEXT , BTCaddress TEXT)")
			cur.execute("""INSERT INTO addresses VALUES(?,?,?)"""
						,(WavesAddress,serializedWallet,BTCWallet['addresses'][0]))
			con.commit()
			# con.close()


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

		con = lite.connect('test.db')
		with con:
			cur = con.cursor()
			# cur.execute("CREATE TABLE IF NOT EXISTS addresses(WavesAddress TEXT , serializedWallet TEXT , BTCaddress TEXT)")
			cur.execute("""SELECT WavesAddress , serializedWallet , BTCaddress 
							FROM addresses WHERE WavesAddress=:adr""",  {"adr": WavesAddress})
			con.commit()

			row = cur.fetchone()
			if row :
				_wallet = get_wallet_addresses(wallet_name=WavesAddress, api_key=self.APIKEY)
				details = get_address_details(_wallet['addresses'][0])
				# print(details)
				txrefs = details['txrefs']
				# print(len(txrefs))
				if len(txrefs) == 0 :
					return {"result" : "not exist any transaction"} 
				else :
					tx_hash = txrefs[0]['tx_hash']					#TODO should be check transaction time
					transaction_details = get_transaction_details(tx_hash)
					receive_count = transaction_details['receive_count']
					# print(tx_hash)
					recipient = pywaves.Address(address=WavesAddress)
					BTC = pywaves.Asset('8LQW8f7P5d5PZM7GtZEBgaqRPGSzS3DfPuiXrURJ4AJS')
					res = self.WAVES.sendAsset(recipient,BTC,receive_count)
				
				return res

		return None





	def CheckTransaction(self,WavesAddress) :
		serializeWlt = None
		#TODO read serializeWlt from DB
		_wallet = get_wallet_addresses(wallet_name=WavesAddress, api_key=APIKEY)

		details = get_address_details(_wallet['addresses'][0])
		tx_hash = details['txrefs'][0]['tx_hash']
		transaction_details = get_transaction_details(tx_hash)
		
		# pyneel.reissueasset(verifywallet())

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
		# print({'key_private': w.get_key().dict()['key_private'] ,'key_public': w.get_key().dict()['key_public']})

# from bitcoinlib import *
from bitmerchant.wallet import Wallet
from blockcypher import create_wallet_from_address,get_address_details,get_wallet_addresses,get_transaction_details ,get_blockchain_overview
import sqlite3 as lite
import pywaves
import blockcypher


from bitmerchant.network import BitcoinTestNet

class BTC(object):
	# network = 'testnet'
	APIKEY = '17536ffbfb674825838e33b77deeec9f'
	WAVES_address ='3NAY7tZhnntswANFCvEhgc9E75PffHSj6gS'
	WAVES_privateKey ='6RqMNnjyNNbCsvXjrtZEJ5yzGbLqEJmrxRzqBupb4R1d'
	coin_symbol = 'btc-testnet'
	# coin_symbol = 'btc'


	def CreateWallet(self,WavesAddress):

		newWallet = Wallet.new_random_wallet(network=BitcoinTestNet)
		# private_key_hex = newWallet.get_private_key_hex()
		# public_key_hex = newWallet.get_public_key_hex()
		serializedWallet = newWallet.serialize()
		newAddress = newWallet.to_address()

		print('newAddress : ' , newAddress)

		BTCWallet = create_wallet_from_address(wallet_name=WavesAddress, address=newAddress, api_key=self.APIKEY , coin_symbol=self.coin_symbol)
		#TODO SAVE WAVESAddress , serializeWlt in DB
		print(BTCWallet)
		con = lite.connect('test.db')
		with con:
			cur = con.cursor()
			cur.execute("CREATE TABLE IF NOT EXISTS addresses(WavesAddress TEXT , serializedWallet TEXT , BTCaddress TEXT , Inventory REAL)")
			cur.execute("""INSERT INTO addresses VALUES(?,?,?,0)"""
						,(WavesAddress,serializedWallet,BTCWallet['addresses'][0]))
			con.commit()
			# con.close()
	


		return {  'addresses'  : BTCWallet['addresses'][0] 
				, 'public_key' : ModuleHandler.encode( newWallet.get_public_key_hex() )  } # public key btc

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
					tx_hash = txrefs[0]['tx_hash']													#TODO should be check transaction time
					transaction_details = get_transaction_details(tx_hash)
					receive_count = transaction_details['receive_count']

					# print(tx_hash)
					recipient = pywaves.Address(address=WavesAddress)
					BTC = pywaves.Asset('DWgwcZTMhSvnyYCoWLRUXXSH1RSkzThXLJhww9gwkqdn')				#todo i dnk?
					WAVES = pywaves.Address(address=self.WAVES_address , privateKey=self.WAVES_privateKey)
					res = WAVES.sendAsset(recipient,BTC,receive_count)								#todo what response
																									#todo dont read serialized? ://

					con = lite.connect('test.db')
					with con:
						cur = con.cursor()
						# cur.execute("CREATE TABLE IF NOT EXISTS btcRemind(BTCaddress TEXT , Inventory REAL ")
						# cur.execute("""INSERT INTO btcRemind VALUES(?,?)""",  (BTCWallet['addresses'][0], receive_count))
						cur.execute(""" UPDATE addresses SET Inventory = ? WHERE WavesAddress = ? """,  ( receive_count , WavesAddress ))
						con.commit()
				
				return res 


		return None





	def SettleTransaction(self,WavesAddress):


		#check transaction WavesAddress and WAVES : attchment BTCaddress and verify assetID
		trnc = ModuleHandler.wrapper("/transactions/address/" + WavesAddress + "/limit/1")
		BTCaddress = trnc[0][0]['attachment']
		if BTCaddress == None :
			return {"result" : "there is not any transaction!" }


		assetDetail = ModuleHandler.wrapper("/assets/details/" + trnc[0][0]['assetId'] )
		decimals = assetDetail['decimals']


		con = lite.connect('test.db')
		with con:
			cur = con.cursor()
			# cur.execute("SELECT MIN(cnt) FROM (SELECT COUNT(*) cnt FROM voting GROUP BY candidate) t;")
			# minimumMigdar = cur.fetchone()
			cur.execute("""SELECT * FROM addresses ORDER BY Inventory DESC """)						#TODO change query for get min count 
			con.commit()
			rows = cur.fetchall()
			cnt = 0
			remind = amount*(10**((-1)*decimals)) #### Decimals Decimals Decimals
			while remind > 0:
				serializedWallet = rows[cnt][1]				#ref to DB structure
				wallet = Wallet.deserialize(serializedWallet)
				inv = rows[cnt][3]

				if inv >= remind :
					
					blockcypher.simple_spend(from_privkey=ModuleHandler.encode( wallet.get_private_key_hex() ) , to_address = BTCaddress , to_satoshis = remind)
					cur.execute(""" UPDATE addresses SET Inventory = ? WHERE WavesAddress = ? """,  ( inv - remind , WavesAddress ))
				

				else :

					blockcypher.simple_spend(from_privkey=ModuleHandler.encode( wallet.get_private_key_hex() ) , to_address = BTCaddress , to_satoshis = inv)
					remind = remind - inv
					cur.execute(""" UPDATE addresses SET Inventory = ? WHERE WavesAddress = ? """,  ( 0 , WavesAddress ))
				con.commit()
			
				
		return res





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
	


	# def CheckTransaction(self,WavesAddress) :
	# 	serializeWlt = None
	# 	#TODO read serializeWlt from DB
	# 	_wallet = get_wallet_addresses(wallet_name=WavesAddress, api_key=APIKEY)

	# 	details = get_address_details(_wallet['addresses'][0])
	# 	tx_hash = details['txrefs'][0]['tx_hash']
	# 	transaction_details = get_transaction_details(tx_hash)
		
	# 	# pyneel.reissueasset(verifywallet())

		# return { None }

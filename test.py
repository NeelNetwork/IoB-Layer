from bitmerchant.wallet import Wallet
from blockcypher import create_wallet_from_address,get_address_details,get_wallet_addresses,get_transaction_details
APIKEY = '17536ffbfb674825838e33b77deeec9f'

import sqlite3 as lite

res ={
    "address": "1DEP8i3QJCsomS4BSMY2RpU1upv62aGvhD", 
    "balance": 4433416, 
    "final_balance": 4433416, 
    "final_n_tx": 7, 
    "n_tx": 7, 
    "total_received": 4433416, 
    "total_sent": 0, 
    "tx_url": "https://api.blockcypher.com/v1/btc/main/txs/", 
    "txrefs": [
        {
            "block_height": 302013, 
            "confirmations": 77809, 
            "confirmed": "datetime.datetime(2014, 5, 22, 3, 46, 25, 0, tzinfo=tzutc())", 
            "double_spend": False, 
            "ref_balance": 4433416, 
            "spent": False, 
            "tx_hash": "14b1052855bbf6561bc4db8aa501762e7cc1e86994dda9e782a6b73b1ce0dc1e", 
            "tx_input_n": -1, 
            "tx_output_n": 0, 
            "value": 20213
        }, 
        {
            "block_height": 302002, 
            "confirmations": 77820, 
            "confirmed": "datetime.datetime(2014, 5, 22, 2, 56, 8, 0, tzinfo=tzutc())", 
            "double_spend": False, 
            "ref_balance": 4413203, 
            "spent": False, 
            "tx_hash": "4cff011ec53022f2ae47197d1a2fd4a6ac2a80139f4d0131c1fed625ed5dc869", 
            "tx_input_n": -1, 
            "tx_output_n": 0, 
            "value": 40596
        }, 
        ...

    ], 
    "unconfirmed_balance": 0, 
    "unconfirmed_n_tx": 0, 
    "unconfirmed_txrefs": []
}


txrefs = res['txrefs']
# print(len(txrefs))
if len(txrefs) == 0 :
    # return {"result" : "not exist any transaction"} 
    pass
else :
    tx_hash = txrefs[0]['tx_hash']                  #TODO should be check transaction time
    transaction_details = get_transaction_details(tx_hash)
    print(transaction_details)
    receive_count = transaction_details['receive_count']
    













#################################################################################################################

# newWallet = Wallet.new_random_wallet()
# # private_key_hex = newWallet.get_private_key_hex()
# # public_key_hex = newWallet.get_public_key_hex()
# serializeWlt = newWallet.serialize()
# newAddress = newWallet.to_address()
# print(serializeWlt)
#TODO SAVE WAVESAddress , serializeWlt in DB
'''
_wallet = get_wallet_addresses(wallet_name="WavesAddressTEST1", api_key=APIKEY)
print(_wallet)
con = lite.connect('test.db')
with con:
    cur = con.cursor()
    # cur.execute("CREATE TABLE IF NOT EXISTS addresses(WavesAddress TEXT , serializedWallet TEXT , BTCaddress TEXT)")
    cur.execute("""SELECT WavesAddress , serializedWallet , BTCaddress FROM addresses WHERE WavesAddress=:s""",  {"s": "WavesAddressTEST"})
    con.commit()

    row = cur.fetchone()
    print(type(row))
    print(row[1])
    print(row[2])
    # con.close()
'''
# trande = {
#     "addresses": [
#         "13XXaBufpMvqRqLkyDty1AXqueZHVe6iyy", 
#         "19YtzZdcfs1V2ZCgyRWo8i2wLT8ND1Tu4L", 
#         "1BNiazBzCxJacAKo2yL83Wq1VJ18AYzNHy", 
#         "1GbMfYui17L5m6sAy3L3WXAtf1P32bxJXq", 
#         "1N2f642sbgCMbNtXFajz9XDACDFnFzdXzV"
#     ], 
#     "block_hash": "0000000000000000c504bdea36e531d8089d324f2d936c86e3274f97f8a44328", 
#     "block_height": 293000, 
#     "confirmations": 86918, 
#     "confirmed": "datetime.datetime(2014, 3, 29, 1, 29, 19, 0, tzinfo=tzutc())", 
#     "double_spend": False, 
#     "fees": 0, 
#     "hash": "f854aebae95150b379cc1187d848d58225f3c4157fe992bcd166f58bd5063449", 
#     "inputs": [
#         {
#             "addresses": [
#                 "1GbMfYui17L5m6sAy3L3WXAtf1P32bxJXq"
#             ], 
#             "output_index": 1, 
#             "output_value": 16450000, 
#             "prev_hash": "583910b7bf90ab802e22e5c25a89b59862b20c8c1aeb24dfb94e7a508a70f121", 
#             "script": "4830450220504b1ccfddf508422bdd8b0fcda2b1483e87aee1b486c0130bc29226bbce3b4e022100b5befcfcf0d3bf6ebf0ac2f93badb19e3042c7bed456c398e743b885e782466c012103b1feb40b99e8ff18469484a50e8b52cc478d5f4f773a341fbd920a4ceaedd4bf", 
#             "script_type": "pay-to-pubkey-hash", 
#             "sequence": 4294967295
#         }, 
#         ...,

#     ], 
#     "lock_time": 0, 
#     "outputs": [
#         {
#             "addresses": [
#                 "1N2f642sbgCMbNtXFajz9XDACDFnFzdXzV"
#             ], 
#             "script": "76a914e6aad9d712c419ea8febf009a3f3bfdd8d222fac88ac", 
#             "script_type": "pay-to-pubkey-hash", 
#             "spent_by": "35832d6c70b98b54e9a53ab2d51176eb19ad11bc4505d6bb1ea6c51a68cb92ee", 
#             "value": 70320221545
#         }
#     ], 
#     "preference": "low", 
#     "received": "datetime.datetime(2014, 3, 29, 1, 29, 19, 0, tzinfo=tzutc())", 
#     "relayed_by": "", 
#     "size": 636, 
#     "total": 70320221545, 
#     "ver": 1, 
#     "vin_sz": 4, 
#     "vout_sz": 1
# }



########################################################### generate private public key #####################################


# wavseAdr='asasasadsdsdsdsdfsdgtrhrytyjj'


# walletList = wallets_list()
# # print(len(l))
# lnames =[ walletList[i]['name'] for i in range(len(walletList)) ]

# # print( DbWallet() )

# if wavseAdr in lnames :

# w = wallet_create_or_open(wavseAdr ,encoding='base58' ,network='testnet')
# print(len(w.get_keys()))
# key = w.get_key(0)
# print(key.key().dict())
# publkey = bytes.fromhex( key.dict()['key_public'] )
# privkey = bytes.fromhex( key.dict()['key_private'] )
# # print(publkey)
# print({'key_private': base58.b58encode(privkey) ,'key_public': base58.b58encode(publkey)})
# print(key.address)

#adr = 

# print(w.deserialize_address(key.address,'base58'))


	# print(w.dict()['key_public'])
	# print(lnames.index(wavseAdr))
# else : 

# 	w = HDWallet.create( wavseAdr ,encoding='base58' ,network='testnet')
# 	print(w.get_key().address)
# 	print({'key_private': w.get_key().dict()['key_private'] ,'key_public': w.get_key().dict()['key_public']})



# res = wallet_delete('Wallet1', force=True)

# l = wallets.wallets_list()

# w = HDWallet.create('MyWallet')

# print(w.get_key())
# print(get_key())

# print(w.info())
print()

# print(l)
print()

# print( w.get_key().wif )
print()

# print(w.get_key())
print()


############################ Handler ###############################
# import sys


# import importlib , logging

# import ModuleHandler


# def str_to_class(module_name, class_name) :
#     class_= None
#     try:
#         module_ = importlib.import_module(module_name)
#         try:
#             class_ = getattr(module_, class_name)()
#         except AttributeError:
#             logging.error('Class does not exist')
#     except ImportError:
#         logging.error('Module does not exist')
#     return class_ or None



# def NewEntry(Type,WavesAdr) :

# 	coin=ModuleHandler.str_to_class('Modules.'+Type, Type)
# 	return coin.createWallet('ssasasassa')






# print(NewEntry('BTC' , 'asasasasasasasa'))
# # b = BTC()
# # print(b.createWallet("asad"))
# res = [
#   [
#     {
#       "type": 11,
#       "id": "Bqp6uVGxb3kSbeAYuAfkMWE8EfRTxYaSBqtkLBh8X819",
#       "sender": "3P2aLcWPWXfs5TEyiGaMht8oLJstvH8BCnU",
#       "senderPublicKey": "GDhSY4xMBbMGhBdCtnnLeYE5z7uDU3iFKroAsxqPacPY",
#       "fee": 4500000,
#       "timestamp": 1551079044372,
#       "proofs": [
#         "3de7KD5kN2EP55vcN2ixbuhHBAs8FsD2QGLKJeN26LPVtaKLtuG1htr89an6HFQT3VEXY5oG9efFeDeM7f3iwajW"
#       ],
#       "version": 1,
#       "assetId": "CHif8iCV1h4VX43vKnUvrm9tEa19xmnXANiwpSiUTt2H",
#       "attachment": "3YUF14",
#       "transferCount": 87,
#       "totalAmount": 174000000000000,
#       "transfers": [
#         {
#           "recipient": "3P9o3ZYwtHkaU1KxsKkFjJqJKS3dLHLC9oF",
#           "amount": 2000000000000
#         }
#       ],
#       "height": 1411869
#     },
#     {
#       "type": 11,
#       "id": "BfMoafpZXB1CEKqQAXHMJyxofuMUb7WDvqAA9cDXHgvx",
#       "sender": "3P2aLcWPWXfs5TEyiGaMht8oLJstvH8BCnU",
#       "senderPublicKey": "GDhSY4xMBbMGhBdCtnnLeYE5z7uDU3iFKroAsxqPacPY",
#       "fee": 4600000,
#       "timestamp": 1551078172302,
#       "proofs": [
#         "5cwQ7jyXb9xPab85GdFwQFJ5NouX7KZWtdEAhvEkNM8zrBdxsgga34pRv1ArzTYzGHkt9xgGvRoU8CfwywY13iAE"
#       ],
#       "version": 1,
#       "assetId": "CHif8iCV1h4VX43vKnUvrm9tEa19xmnXANiwpSiUTt2H",
#       "attachment": "45Uvok",
#       "transferCount": 90,
#       "totalAmount": 180000000000000,
#       "transfers": [
#         {
#           "recipient": "3P9o3ZYwtHkaU1KxsKkFjJqJKS3dLHLC9oF",
#           "amount": 2000000000000
#         }
#       ],
#       "height": 1411854
#     }
#   ]
# ]

# import requests

# OFFLINE = False
# NODE = 'https://nodes.wavesnodes.com'

# def wrapper(api, postData='', host='', headers=''):
#     global OFFLINE
#     if OFFLINE:
#         offlineTx = {}
#         offlineTx['api-type'] = 'POST' if postData else 'GET'
#         offlineTx['api-endpoint'] = api
#         offlineTx['api-data'] = postData
#         return offlineTx
#     if not host:
#         host = NODE
#     if postData:
#         req = requests.post('%s%s' % (host, api), data=postData, headers={'content-type': 'application/json'}).json()
#     else:
#         req = requests.get('%s%s' % (host, api), headers=headers).json()
#     return req

# s = wrapper("/transactions/address/3P9o3ZYwtHkaU1KxsKkFjJqJKS3dLHLC9oF/limit/1")

# print (s[0][0]['attachment'])
from bitmerchant.wallet import Wallet
from bitmerchant.network import BitcoinTestNet

import sqlite3 as lite

import ModuleHandler




APIKEY = '17536ffbfb674825838e33b77deeec9f'
WAVES_address ='3NAY7tZhnntswANFCvEhgc9E75PffHSj6gS'
WAVES_privateKey ='6RqMNnjyNNbCsvXjrtZEJ5yzGbLqEJmrxRzqBupb4R1d'
coin_symbol = 'btc-testnet'
# coin_symbol = 'btc'
CHAIN = 'testnet' #'mainnet'
TESTNET_NODE = 'https://testnode1.wavesnodes.com'

# con = lite.connect('test.db')
# with con:
#   cur = con.cursor()
#   # cur.execute("CREATE TABLE IF NOT EXISTS addressid(id INTEGER PRIMARY KEY AUTOINCREMENT, WavesAddress TEXT  NOT NULL )")
#   # cur.execute("""INSERT INTO addressid (WavesAddress) VALUES(?)""",(WavesAddress,))
#   # cur.execute("""SELECT * FROM addressid """)
#   cur.execute("SELECT * FROM  addresses")

#   con.commit()
#   rows = cur.fetchall()

#   for row in rows:
#     # wallet = Wallet.deserialize(row[1])
#     wallet = Wallet.deserialize(row[1] ,  network=BitcoinTestNet)
#     print(row[1])
#     print('private  : ', ModuleHandler.encode(wallet.get_private_key_hex()))
#     print('public  : ', ModuleHandler.encode(wallet.get_public_key_hex()))
#   # print(row)
from blockcypher import create_wallet_from_address,get_address_details,get_wallet_addresses,get_transaction_details ,get_blockchain_overview

# for i in range(1,11) : 
#   _wallet = get_wallet_addresses(wallet_name='Noay'+ str(i), api_key=APIKEY , coin_symbol=coin_symbol)
#   print('_wallet',_wallet)


details = get_address_details('mkBPyZ5V25kzzJkQZg5EzQVeVduonrpqNU' , coin_symbol=coin_symbol)
print(details)


{'confirmations': 21, 'preference': 'high', 'total': 16163340269, 'fees': 16922, 
'hash': 'f20d44c267889206f8735a2ff57b84d549beb07bc18c3c7c22c7f947debfd666', 'lock_time': 1482213, 
'outputs': [{'value': 16152611376, 'script_type': 'pay-to-script-hash', 
            'spent_by': 'fa9c639299a960b543e3dbb38bec505d45ff60f8d3a995932e82f7ef570d47b5', 
            'script': 'a914ff86b9a980517a61237460dc86f3fffa565eae8a87', 
            'addresses': ['2NGYKh5HTaaeRu3mVnMEM5cP4cMLZjP21VK']}, 

            {'value': 10728893, 'script_type': 'pay-to-pubkey-hash', 'script': '76a9143325bf43d852dfcd57deea0afeab7957152f3c0d88ac', 
                                'addresses': ['mkBPyZ5V25kzzJkQZg5EzQVeVduonrpqNU']}]

, 'block_height': 1482214, 'vin_sz': 1,
'received': datetime.datetime(2019, 2, 28, 12, 15, 36, 580000, tzinfo=tzutc()),
'addresses': ['2N4BEpd3Yc5fpAk4P3dxNWqgJ8dduFPuruc', '2NGYKh5HTaaeRu3mVnMEM5cP4cMLZjP21VK', 'mkBPyZ5V25kzzJkQZg5EzQVeVduonrpqNU'], 
'vout_sz': 2, 'inputs': [{'script_type': 'pay-to-script-hash', 'sequence': 4294967294, 
'script': '160014f9b555e618377bfd41aae33727ac10816780981f', 'prev_hash': 'c6459b5557df44aaf8e31e566d5bb61356102b8a021bc699d76ea20ade8df123',
'output_index': 0,
'witness': ['3045022100827ed890c20a2cce1171b91a097a5fab9f447a5ba2f31ee6ce3aae3cbfee4487022013ae0c123be0fcd1cba43ef105f23d7180f218cf8acb30196bb46b18113ff27c01', 
'028b5c1b9177aaf40302e1cac59aa3f45c58e93ba2921ccaab757f243fbee235b2'], 'age': 1482212, 'output_value': 16163357191, 
'addresses': ['2N4BEpd3Yc5fpAk4P3dxNWqgJ8dduFPuruc']}], 'size': 140, 'confidence': 1, 
'block_hash': '0000000000000001d9b9730df267cb2e85bae7fc70c7fe85c833ea9975c8946f', 
'confirmed': datetime.datetime(2019, 2, 28, 12, 17, 13, tzinfo=tzutc()), 'block_index': 4, 
'ver': 2, 'relayed_by': '5.9.144.44:18333', 'double_spend': False}
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
import sqlite3 as lite

con = lite.connect('test.db')
with con:
  cur = con.cursor()
  # cur.execute("CREATE TABLE IF NOT EXISTS addressid(id INTEGER PRIMARY KEY AUTOINCREMENT, WavesAddress TEXT  NOT NULL )")
  # cur.execute("""INSERT INTO addressid (WavesAddress) VALUES(?)""",(WavesAddress,))
  cur.execute("""SELECT * FROM addressid """)
  con.commit()
  row = cur.fetchall()

  print(row)

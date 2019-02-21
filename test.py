from bitcoinlib import * 
from bitcoinlib.wallets import *
import base58


wavseAdr='asasasadsdsdsdsdfsdgtrhrytyjj'


# walletList = wallets_list()
# # print(len(l))
# lnames =[ walletList[i]['name'] for i in range(len(walletList)) ]

# # print( DbWallet() )

# if wavseAdr in lnames :

w = wallet_create_or_open(wavseAdr ,encoding='base58' ,network='testnet')
print(len(w.get_keys()))
key = w.get_key(0)
print(key.key().dict())
publkey = bytes.fromhex( key.dict()['key_public'] )
privkey = bytes.fromhex( key.dict()['key_private'] )
# print(publkey)
print({'key_private': base58.b58encode(privkey) ,'key_public': base58.b58encode(publkey)})
print(key.address)

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
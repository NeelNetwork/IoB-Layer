from bitcoinlib import * 
from bitcoinlib.wallets import *


wavseAdr='asasasadsdsdsdsdfsdgtrhrytyj'


walletList = wallets_list()
# print(len(l))
lnames =[ walletList[i]['name'] for i in range(len(walletList)) ]

# print( DbWallet() )

if wavseAdr in lnames :

	w = HDWallet(wavseAdr)
	# print(w.info())
	print(w.get_key().address)
	print({'key_private': w.get_key().dict()['key_private'] ,'key_public': w.get_key().dict()['key_public']})
	# print(w.dict()['key_public'])
	# print(lnames.index(wavseAdr))
else : 

	w = HDWallet.create( wavseAdr ,  network='testnet')
	print(w.get_key().address)
	print({'key_private': w.get_key().dict()['key_private'] ,'key_public': w.get_key().dict()['key_public']})



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
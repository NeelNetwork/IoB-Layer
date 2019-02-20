from bitcoinlib import * 

w = wallets.wallet_create_or_open_multisig('Wallet1',None)
l = wallets.wallets_list()

print(w.get_key().address , w.get_key().wif , w.get_key())
print(l)


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
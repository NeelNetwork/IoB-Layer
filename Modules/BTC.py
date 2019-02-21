from bitcoinlib import *


class BTC(object):

    def createWallet(self,WavesAddress):

    	walletList = wallets_list()
    	# print(len(l))
		lnames =[ walletList[i]['name'] for i in range(len(walletList)) ]
		if wavseAdr in lnames :
			w = HDWallet(wavseAdr)
			print(w.get_key().address)
			return {'address' : w.get_key().address }
			# print({'key_private': w.get_key().dict()['key_private'] ,'key_public': w.get_key().dict()['key_public']})
			# print(w.dict()['key_public'])
			# print(lnames.index(wavseAdr))
			# print(w.info())
		else : 
			w = HDWallet.create( wavseAdr ,  network='testnet')
			print(w.get_key().address)
			return {'address' : w.get_key().address }

			# print({'key_private': w.get_key().dict()['key_private'] ,'key_public': w.get_key().dict()['key_public']})
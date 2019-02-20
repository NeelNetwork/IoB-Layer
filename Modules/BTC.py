from bitcoinlib import *


class BTC(object):

    def createWallet(self,WavesAddress):
    	# return " createWallet WavesAddress"
    	w = wallets.wallet_create_or_open_multisig( WavesAddress , None , network='testnet')
    	return w.get_key().address



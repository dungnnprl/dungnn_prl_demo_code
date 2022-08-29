from web3 import Web3
import time
from web3.middleware import geth_poa_middleware

bsc_testnet = 'https://data-seed-prebsc-1-s1.binance.org:8545/'

web3 = Web3(Web3.HTTPProvider(bsc_testnet))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)  #  Inject poa middleware
def transactionChecker(account_address):
    block = web3.eth.getBlock('latest')
    if (block is not None and block.transactions is not None) :
        for txHash in block.transactions :
            tx = web3.eth.getTransaction(txHash)
            if(tx["from"] == account_address):
                print("New Transaction from my address ")  
                print("Transaction Id ",tx["hash"]) 
                print("To ",tx["to"]) 
                print("Value ",tx["value"]) 
            if(tx["to"] == account_address):
                print("New Transaction to my address ")  
                print("Transaction Id ",tx["hash"]) 
                print("From ",tx["from"]) 
                print("Value ",tx["value"]) 
from web3 import Web3
import time
from web3.middleware import geth_poa_middleware

from checkTransactionInBlock import transactionChecker

bsc_testnet = 'https://data-seed-prebsc-1-s1.binance.org:8545/'
account_address = '0x5A8E6d0642D9E0875A0886903f069622177DE04c'
account_private_key = '5b584e5eeb23b603661569b04509c7bd2394b4fb5ef5011f698dccf33b041777'

web3 = Web3(Web3.HTTPProvider(bsc_testnet))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)  #  Inject poa middleware
interval = 600000

def log_loop(address,interval):
    while True:
        transactionChecker(address)
        #time.sleep(interval)

log_loop(account_address,interval)
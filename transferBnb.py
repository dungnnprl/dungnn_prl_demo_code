from web3 import Web3
from web3.middleware import geth_poa_middleware
import json

bsc = 'https://bsc-dataseed.binance.org/'
bsc_testnet = 'https://data-seed-prebsc-1-s1.binance.org:8545/'
account_address = '0x5A8E6d0642D9E0875A0886903f069622177DE04c'
account_address_2 = '0x135A7348F0556e0B8f8Ad1a1CC4F755B04651a4d'
account_private_key = '5b584e5eeb23b603661569b04509c7bd2394b4fb5ef5011f698dccf33b041777'

web3 = Web3(Web3.HTTPProvider(bsc_testnet))
#web3.middleware_onion.inject(geth_poa_middleware, layer=0)  #  Inject poa middleware

account = web3.eth.account.privateKeyToAccount(account_private_key)
balance = web3.fromWei(web3.eth.getBalance(account_address),'ether')
nonce = web3.eth.getTransactionCount(account_address)
print("----------------------------------------------------------------------------------------------")
print("Address : ",account.address)
print("--------")
print("Balance : ",balance)
print("--------")
print("Total Transaction : ",nonce)
print("--------")
print("Total Checksum address : ",web3.toChecksumAddress(account_address))
print("----------------------------------------------------------------------------------------------")

tx = {
    'nonce': nonce,
    'value': web3.toWei(0.1,'ether'),
    'to': account_address_2,
    'gas': 100000,
    'gasPrice': web3.toWei(100,'gwei') 
}

signed_tx = web3.eth.account.signTransaction(tx,account_private_key)
tx_transaction = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print("Transaction success with hash : ",web3.toHex(tx_transaction))
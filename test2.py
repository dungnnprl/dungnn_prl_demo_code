from web3 import Web3
import json

bsc = 'https://bsc-dataseed.binance.org/'
test_address ='0x0D0707963952f2fBA59dD06f2b425ace40b492Fe'
txn_hash = '0x3344325b1aad76bc0ddb42e7b77ef8bb31315bbcecd4083f4d0db5aaaeb7c9a9'
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())

#Nonce
nonce = web3.eth.getTransactionCount(test_address) 
print('Nonce :',nonce)
print('Balance of ',web3.eth.get_balance(test_address))

print('Transaction ',web3.eth.getTransaction(txn_hash))


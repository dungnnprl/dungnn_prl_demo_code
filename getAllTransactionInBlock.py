from web3 import Web3
from web3.middleware import geth_poa_middleware
import json

data ={} 
block_num = 20516609
block_num_once = 1
bsc = 'https://bsc-dataseed.binance.org/'
bsc_testnet = 'https://data-seed-prebsc-1-s1.binance.org:8545/'
web3 = Web3(Web3.HTTPProvider(bsc))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)  #  Inject poa middleware
print(web3.isConnected())

print('Total transaction in block',block_num_once,':',web3.eth.getBlockTransactionCount(block_num_once))

lastest = web3.eth.blockNumber
block = web3.eth.getBlock(block_num_once)
hash = block.hash
list_trasaction = block.transactions

print("Block  : ",block)
block = web3.eth.getBlock(block_num_once)
print("-----------------------------------")
print("Hash block use block.hash : ",web3.toHex(hash))
print("-----------------------------------")
list_trasaction_json = json.loads(web3.toJSON(list_trasaction))
print("Transaction in block : ",block_num_once)
for transaction in list_trasaction_json:
    print("Transaction : ",transaction)
from ast import arguments
from web3 import Web3
from web3.middleware import geth_poa_middleware
import constant
web3 = Web3(Web3.HTTPProvider(constant.bsc_testnet))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)  #  Inject poa middleware
latest = web3.eth.blockNumber
print(web3.isConnected())

#Token Box1 info


contract_instance = web3.eth.contract(address = constant.contract_address_box1,abi = constant.abi_box1)

block_test = 21655492  
transaction_type = 'Normal'
transfer_filter = contract_instance.events.Transfer.createFilter(fromBlock=block_test,toBlock=block_test)
logs = transfer_filter.get_all_entries()
print("Total Transaction : ",len(logs))
#print("Logs : ",logs)
for log in logs :
    if(log['args']['to'] == constant.address_0x0):
        transaction_type = 'Burn'
    if(log['args']['from'] == constant.address_0x0):
        transaction_type = 'Mint'     
    # if(log['args']['from'] == constant.contract_address_box1):
    #     transaction_type = 'Withdraw'  
    # if(log['args']['to'] == constant.contract_address_box1):
    #     transaction_type = 'Deposit'                   
    print("Transaction : ",web3.toHex(log['transactionHash']))
    print("Transaction type : ",transaction_type)
    print("Event : ",log['event'])
    print("From : ",log['args']['from'])
    print("To : ",log['args']['to'])
    print("TokenId : ",log['args']['tokenId'])
    transaction = web3.eth.getTransaction(web3.toHex(log['transactionHash']))
    #print(transaction)
    print("Gas : ",transaction['gas'])  
    print("Nonce : ",transaction['nonce'])
    print("###########################################################")       

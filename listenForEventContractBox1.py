from web3 import Web3
from web3.middleware import geth_poa_middleware
import asyncio
import constant
web3 = Web3(Web3.HTTPProvider(constant.bsc_testnet))
web3.middleware_onion.inject(geth_poa_middleware, layer=0)
contract_instance = web3.eth.contract(address = constant.contract_address_box1,abi = constant.abi_box1)
latest = web3.eth.blockNumber
transaction_type = 'Normal'

def handle_event(event):
    if(event['args']['to'] == constant.address_0x0):
        transaction_type = 'Burn'
    if(event['args']['from'] == constant.address_0x0):
        transaction_type = 'Mint'                  
    print("Transaction : ",web3.toHex(event['transactionHash']))
    print("Transaction type : ",transaction_type)
    print("Event : ",event['event'])
    print("From : ",event['args']['from'])
    print("To : ",event['args']['to'])
    print("TokenId : ",event['args']['tokenId'])
    print("###########################################################")         

async def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        await asyncio.sleep(poll_interval)

def main():
    transfer_filter = contract_instance.events.Transfer.createFilter(fromBlock=latest)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(
            asyncio.gather(
               log_loop(transfer_filter, 3)    
            )
        )
    finally:
        loop.close()
if __name__ == '__main__':
    main()
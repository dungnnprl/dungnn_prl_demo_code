def get_database(db_name):
    from pymongo import MongoClient
    import pymongo

    CONNECTION_STRING = "mongodb://cluster-read:at5M8RO2IG1mFTK4c8EPfbiy@prod1.silotech.vn:28000,prod2.silotech.vn:28000,prod3.silotech.vn:28000/cluster?replicaSet=replicaset-remote&authSource=admin&readPreference=secondary&maxStalenessSeconds=120"

    from pymongo import MongoClient
    client = MongoClient(CONNECTION_STRING)

    return client[db_name]
    
if __name__ == "__main__":    
    db_name = 'prl-box-prod-testnet-public-2'
    db_testnet = get_database(db_name)
    rewards = db_testnet['rewards'].find({'reward_to_owner':"0x743A38774Ce5dFE808551f5900EfE87743b398Fc"}).limit(10)
    for reward in rewards:
        print("Id : ",reward["_id"])

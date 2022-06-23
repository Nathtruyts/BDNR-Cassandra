import redis
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider

def connectCassandra():
    cloud_config= {
            'secure_connect_bundle': '<</PATH/TO/>>secure-connect-nerve01.zip'
    }

    auth_provider = PlainTextAuthProvider('#client id#', '..r,B9TelMAjK00mfH4smLv50-BXQsWgmWsQeP+_TWv.4OPZ_soLmS73tI_djiX1RTKLUCKd8MnAxQa5USMZZ7u1oJXEcu5gLMICQZouNBOnTqepQmXGfUjai3KRlrIU')
    cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
    session = cluster.connect()
    
    return session

def connectRedis():
    myRedis = redis.StrictRedis(
        host= 'redis-10018.c299.asia-northeast1-1.gce.cloud.redislabs.com',
        port= '10018',
        password= 'password',
    )
    return myRedis
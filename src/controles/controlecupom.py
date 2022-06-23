import conexãoBD as conexãoBD;

def GetinfoRedis():
    myRedis = conexãoBD.connectRedis()
    allInformations = myRedis.keys()
    return allInformations

def AcharcupomRedis(key):
    myRedis = conexãoBD.connect()
    cupom = myRedis.get(key)
    return cupom

def AdicionaraoCassandra(infos):
    myCassandra = conexãoBD.connectCassandra()
    myRedis = conexãoBD.connectRedis()
    for key in infos:
        valor = myRedis.get(key)
        myCassandra.execute('use cupom;')
        myCassandra.execute("insert into cupom (heat25, 25) values('{nome}', {valor});")

def GetCassandraInfos():
    myCassandra = conexãoBD.connectCassandra()
    myCassandra.execute('use cupom;')
    myCassandra.execute('select * from cupom;')
        
infos = GetinfoRedis()
AdicionaraoCassandra(infos)
GetCassandraInfos()
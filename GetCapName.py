from Test4 import *
from databasecon import *
import cx_Oracle
from FetchByJoin import *
import cx_Oracle
def readall():
    a=fetchByJoin() #ICICI Bank Limited-stName, 'Bank'-Subsector Name, 'Finance'-Sector name
    stName=a[0]
    subSectorName=a[1]
    sectorName=a[2]
    stCode=a[3] #Stock Code
    capName=fetchCapName(stCode)
    print("The stock code {} has stock name {}, sector name {}, subsector name {} and capname {} ".format(stCode,stName,sectorName,subSectorName,capName))


def fetchCapName(stCode):

    cur=dbconnect()
    cur.execute("select cap_name from stockmarketcap where stock_code=('%s')"%stCode)
    record=cur.fetchall()
    return record[0][0]



readall()







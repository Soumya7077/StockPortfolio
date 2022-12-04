import cx_Oracle
from StockPortfolioConst import *
def sectorMasterFetch():
    try:
        con = cx_Oracle.connect(const.DB_CONNECT)
        cur = con.cursor()
        cur.execute("select id,name,parentid from sectormaster")
        records = cur.fetchall()
        dictSector={}
        for column in records:
            id=column[0]
            name=column[1]
            parentId=column[2]
            sectorDictObj={id:(name,parentId)}

            dictSector.update(sectorDictObj)

        stockCode=input("Enter Stock Code:").upper()
        cur.execute("select name,code,subcategory from stocksmaster where code=('%s')"%(stockCode))
        records=cur.fetchall()

        stName=records[0][0] #Stock Name
        stCode=records[0][1] #Stock Code
        subCatId=records[0][2]#Sub Category id
        #print(stName)
        #print(stCode)
        #print(subCatId)

        getValOfSubSec=dictSector.get(subCatId)#Sector Name & Parent id
        subSectorName=getValOfSubSec[0] #Sub Sector Name
        parentID=getValOfSubSec[1]
        getValOfSec=dictSector.get(parentID) #Sector Name
        print("The Stock Code {} has stock name {} , Sub Sector Name {} and Sector name {}".format(stockCode,stName,subSectorName,getValOfSec[0]))



    except cx_Oracle.DatabaseError as db:
        print("Error in Database",db)





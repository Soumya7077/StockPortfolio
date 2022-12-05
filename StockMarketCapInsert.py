import csv, cx_Oracle
from StockPortfolioConst import *
def marketCapMaster():
    try:
        r=int(input("Enter value"))
        con = cx_Oracle.connect(const.DB_CONNECT)
        cur = con.cursor()
        cur.execute("select id,marketcap_in_crores,capname from marketcapmaster where marketcap_in_crores between lower and upper=(%d)"%(r))
        records=cur.fetchall()
        for column in records:
            #print(column)
            id=column[0]
            marketCapInCrores=column[1]
            capName=column[2]
            if (r==marketCapInCrores):
                print(capName)




    except cx_Oracle.DatabaseError as db:
        print("Error in Database",db)

marketCapMaster()







"""def readCsvInsert():
    try:
        with open(input("Enter the path of the file:"), "r") as fp:
            cr = csv.reader(fp)
            cr.__next__()
            for record in cr:
                print(record)
                id=record[0]
                stCode = record[1]
                stName = record[2]
                marketCap=record[3]


                try:
                    con = cx_Oracle.connect(const.DB_CONNECT)
                    cur = con.cursor()
                    cur.execute("insert into stockdetails values ('%s','%s')" % (stCode, stName))
                    cur.execute("insert into stockmarketcap values (%d,'%s','%s')" %(id,stCode,marketCap))
                    con.commit()
                    print()
                except cx_Oracle.DatabaseError as db:
                    print("Can not insert the data in database", db)


    except FileNotFoundError:
        print("File does not exist")



readCsvInsert()"""
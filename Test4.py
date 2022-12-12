import csv, cx_Oracle
from StockPortfolioConst import *
def marketCapMaster(marketCapAmount):

    try:
        con = cx_Oracle.connect(const.DB_CONNECT)
        cur = con.cursor()
        cur.execute("select capname from marketcapmaster where %d between lower_marketcap and higher_marketcap"%(marketCapAmount))
        records=cur.fetchall()
        for column in records:
            capName = column[0]
            return capName


    except cx_Oracle.DatabaseError as db:
        print("Error in Database",db)
# Add a new menu, which will take input as multiple stock codes(comma separated value) and gives output accordingly
import cx_Oracle
from StockPortfolioConst import *
from FetchAll import *


def getStockDetails(stockCode):
    try:
        printStockDetailsBasedOnCode(stockCode)
        print("The stock code {} has stock name- {}, having subcategory as {} and with Sector as {}".format(stockCode,
                                                                                                            stName,
                                                                                                            subCatDictVal[
                                                                                                                1],
                                                                                                            catDictVal))


    except Exception as e:
        print("We could not find search item please try again")
        print(e)


def mulInput():
    r = input("Enter stock code:").upper()
    return r


def getStockDetails():
    a = mulInput()
    if (len(a) == 1):
        printStockDetailsBasedOnCode(a)
    else:
        # a=getStockDetails(a.split(","))
        s = a.split(",")
        for i in s:
            printStockDetailsBasedOnCode(i)

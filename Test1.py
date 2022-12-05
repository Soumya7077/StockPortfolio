import cx_Oracle


def dbconnect():
    con = cx_Oracle.connect("c##babul/soumya@localhost/orcl")
    cur = con.cursor()
    cur.execute("select s1.name as sector_name,s2.name as subsector_name,s1.id as parent_id,s2.id as id,sm.stock_code as code,sm.stock_name as stock_name from sectormaster s1 inner join sectormaster s2 on s1.id=s2.parentid inner join stockmaster sm on s2.id = sm.subcategory_id")
    records = cur.fetchall()
    r = input("Enter Stock Code:").upper()
    for column in records:
        if (r == column[4]):
            sectorName = column[0]
            subSectorName = column[1]
            parentId=column[2]
            id = column[3]
            stockCode=column[4]
            stockName=column[5]


    print("Stock Code:{},Stock Name:{},SubcategoryName:{},Category Name:{}".format(stockCode, stockName, subSectorName,
                                                                                   sectorName))


dbconnect()

import cx_Oracle


def dbconnect():
    con = cx_Oracle.connect("c##babul/soumya@localhost/orcl")
    cur = con.cursor()
    cur.execute(
        " select s1.name,s2.name from sectormaster s1 inner join sectormaster s2  on s1.id=s2.parentid where s2.parentid is not null")
    records = cur.fetchall()
    for column in records:
        sectorName = column[0]
        subSectorName = column[1]

    cur.execute(
        "select st.name,st.code,s.subcategoryname,s.subcategoryid from stocksmaster st,subcategorymaster s where st.subcategory=s.subcategoryid")
    records1 = cur.fetchall()
    r = input("Enter Stock Code:").upper()
    for c in records1:
        if (r == c[1]):
            stname = c[0]  # Stock name
            stCode = c[1]  # Stock Code
            subCategoryName = c[2]  # Subcategory name
            subCategoryid = c[3]  # Subcategory id"""


dbconnect()

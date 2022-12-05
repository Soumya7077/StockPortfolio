from databasecon import db

cur = db()
cm = cur.execute("select categoryid,categoryname from categorymaster")
scum = cur.execute("select subcategoryid,categoryid,subcategoryname from subcategorymaster")
sm = cur.execute("select subcategory,name,code from stocksmaster")
records = cur.fetchall()
records1 = cur.fetchall()
records2 = cur.fetchall()
records3 = cur.fetchall()

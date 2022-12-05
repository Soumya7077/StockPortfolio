import cx_Oracle


def db():
    con = cx_Oracle.connect("c##babul/soumya@localhost/orcl")
    cur = con.cursor()
    return cur

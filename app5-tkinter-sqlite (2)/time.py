import sqlite3
from datetime import datetime
def connect():
    conn=sqlite3.connect("FF.db")
    cur=conn.cursor()
    cur.execute(" ('create table foo (barinteger, baztimestamp)")
    conn.commit()
    conn.close()


def view():
    conn=sqlite3.connect("FF.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM foo")
    rows=cur.fetchall()
    conn.close()
    return rows
#
#
# def insert(barinteger, baztimestamp):
#     conn=sqlite3.connect("FF.db")
#     cur=conn.cursor()
#     cur.execute("INSERT INTO 'insert into foo values(?, ?)'", (23, datetime.datetime.now()))
#     conn.commit()
#     conn.close()

print(view())


# def search(d1,d2):
#     conn=sqlite3.connect("time.db")
#     cur=conn.cursor()
#     cur.execute("SELECT * FROM datetimetext WHERE d1, typeof(d1), d2, typeof(d2)", (d1,d2))
#     rows=cur.fetchall()
#     conn.close()
#     return rows


# print(view())
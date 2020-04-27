import sqlite3
import  datetime


def connect():
    conn=sqlite3.connect("books3.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year datetime, isbn integer, time dateime)")
    conn.commit()
    conn.close()

def insert(title,author,year,isbn, time):
    conn=sqlite3.connect("books3.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?)",(title,author,year,isbn,time))
    conn.commit()
    conn.close()

def insert2(title,author,year,isbn, time):
    conn=sqlite3.connect("books3.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?,?)",(title,author,year,isbn, time))
    conn.commit()
    conn.close()



def view():
    conn=sqlite3.connect("books3.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book")
    rows=cur.fetchall()
    conn.close()
    return rows

# def search(title="",author="",year="",isbn=""):
#     conn=sqlite3.connect("books.db")
#     cur=conn.cursor()
#     cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title,author,year,isbn))
#     rows=cur.fetchall()
#     conn.close()
#     return rows

##################This belows dearch is work

def search():
    conn=sqlite3.connect("books2.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM book WHERE year > 'now' AND author='John Smith'",())
    rows=cur.fetchall()
    conn.close()
    return rows
now = datetime.datetime.now().replace(hours=0, minute=0, microsecond=0)

#
# ##################This belows dearch is work
#
# def search():
#     conn=sqlite3.connect("books3.db")
#     cur=conn.cursor()
#     cur.execute(f"SELECT * FROM book WHERE  year < 'datetime'")
#     rows=cur.fetchall()
#     conn.close()
#     return rows
# print(search())
# now = datetime.now()
# datetime

# AND title='oonnnnoo'
#######################################################
#
def delete(id):
    conn=sqlite3.connect("books3.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    conn.commit()
    conn.close()
#
def update(id,title,author,year,isbn):
    conn=sqlite3.connect("books3.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    conn.commit()
    conn.close()

#################

def update2(id,title):
    conn=sqlite3.connect("books3.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title=? WHERE id=?",(title,id))
    conn.commit()
    conn.close()

def update4():
    conn=sqlite3.connect("books3.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title='' WHERE id=2")
    conn.commit()
    conn.close()

def update5(id):
    conn=sqlite3.connect("books3.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title='' WHERE id=?",id)
    conn.commit()
    conn.close()




def update6(id,year,isbn,time):
    conn=sqlite3.connect("books3.db")
    cur=conn.cursor()
    cur.execute("UPDATE book SET title='', author='', year=?, isbn=?, time=? WHERE id=?",(year,isbn,time,id))
    conn.commit()
    conn.close()




# def update3(title='oonnnnoo'):
#     conn=sqlite3.connect("books2.db")
#     cur=conn.cursor()
#     cur.execute(f" UPDATE book SET author='2' WHERE title='{title}'")
#     rows=cur.fetchall()
#     conn.close()

# update3()

# def update7(author=""):
#     conn=sqlite3.connect("books2.db")
#     cur=conn.cursor()
#     cur.execute(f" UPDATE book SET \'{author}\' =\'{'love'}\'")
#     rows=cur.fetchall()
#     conn.close()
# # WHERE title='{title}
# update7()

# \'{Column}\' =\'{Info}\'

# UPDATE book SET title='' WHERE title ='The moon'
# update2(1,'')
# update4()
# update5('5')
#
#
# update3('3')
#


# print(view())

#
#
# # def bserach(title="Hey there"):
# #     conn=sqlite3.connect("books.db")
# #     cur=conn.cursor()
# #     cur.execute(f"SELECT * FROM book WHERE  title='{title}'")
# #     rows=cur.fetchall()
# #     conn.close()
# #     return rows
# # # title=""
# # # title='{title}' OR
# #
# # print(bserach())

connect()
# print(search('John Smith'))
# now = datetime.now()





insert("oonnnnoo","John Smith",'2020-01-13 15:00:00', 999999,now )
insert("oonnnnoo","John Smith",'2015-01-13 15:00:00', 999999,now )
# # delete(3)
# # update(4,"The moon","John Smooth",1917,99999)
# # print(view())
# # print(search(title="jj"))

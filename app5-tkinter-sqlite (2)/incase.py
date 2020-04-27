import sqlite3


import sqlite3


# db1 = sqlite3.connect("my.db")
# cursor = db1.cursor()
#
# cursor.execute("DROP TABLE IF EXISTS my_table")
#
# sql = '''CREATE TABLE my_table (
#         name TEXT DEFAULT NULL,
#         value INT
#         );'''
# cursor.execute(sql)
#
# sql = ("CREATE INDEX index_my_table ON my_table (name);")
# cursor.execute(sql)
# db1.commit()
# db1.close()





def connect():
    conn=sqlite3.connect("Cinema6.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Booking (Movieid INTEGER PRIMARY KEY, Movietittle TEXT, Genredescription TEXT, Viewingtimes DATETIME, SEAT VARCHAR, STATUS TEXT, CUSTOMERFIRSTNAME TEXT, CUSTOMERLASTNAME TEXT,EMAIL VARCHAR, PRICE integer ) ")
    # EMAIL TEXT)")
    conn.commit()
    conn.close()



def connect():
    conn=sqlite3.connect("Cinema6.db")
    cur=conn.cursor()
    cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS Moviecreation ON Booking (Movietittle, Viewingtimes , SEAT)")
    conn.commit()
    conn.close()


#
# # def connect():
# #     conn=sqlite3.connect("Cinema.db")
# #     cur=conn.cursor()
# #     cur.execute("DROP INDEX  Moviecreation" )
# #     conn.commit()
# #     conn.close()
#
#
# #
def insert(Movietittle , Genredescription, Viewingtimes, SEAT,STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME):  # ,STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL):
    conn=sqlite3.connect("Cinema5.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'A',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) #CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'B',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME))#,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'C',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) #,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'D',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)),#CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'E',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) #,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'F',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) #,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'G',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) #,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'H',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) #CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'I',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) #,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'J',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) # ,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'K',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) # ,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'L',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME))  #,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'M',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) #,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'N',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) #CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'O',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) #CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'Q',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) # CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'R',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) #CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'S',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) # CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'T',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) # CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'U',STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME)) #CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    conn.commit()
    conn.close()
    view()

# def view():
#     conn=sqlite3.connect("Cinema5.db")
#     cur=conn.cursor()
#     cur.execute("SELECT * FROM Booking")
#     rows=cur.fetchall()
#     conn.close()
#     return rows
# #
# def search(Movietittle="" , Genredescription="", Viewingtimes="", SEAT="",STATUS="" ,CUSTOMERFIRSTNAME="", CUSTOMERLASTNAME=""): # ) :  STATUS="" CUSTOMERFIRSTNAME="", CUSTOMERLASTNAME=""):, # EMAIL="", STATUS=""):### THere search in case they so an search.
#     conn=sqlite3.connect("Cinema5.db")
#     cur=conn.cursor()
#     cur.execute("SELECT * FROM Booking WHERE Movietittle=? OR  Genredescription=? OR Viewingtimes=? OR SEAT=?  OR STATUS=? OR CUSTOMERFIRSTNAME=? OR CUSTOMERLASTNAME=?  " ,(Movietittle , Genredescription, Viewingtimes, SEAT, STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME )) #, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
#     rows=cur.fetchall()
#     conn.close()
#     return rows
#
# # # OR CUSTOMERFIRSTNAME=? OR CUSTOMERLASTNAME=? , STATUS=? OR EMAIL=? OR STATUS=?
# #
# def delete(Movieid):
#     conn=sqlite3.connect("Cinema5.db")
#     cur=conn.cursor()
#     cur.execute("DELETE FROM Booking WHERE Movieid  =?",(Movieid,))
#     conn.commit()
#     conn.close()
# # #
# def update(Movieid,Movietittle , Genredescription, Viewingtimes, SEAT, STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME ):  ##, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS):
#     conn=sqlite3.connect("Cinema5.db")
#     cur=conn.cursor()
#     cur.execute("UPDATE Booking SET Movietittle=?, Genredescription=?, Viewingtimes=?, SEAT=?, STATUS=?,CUSTOMERFIRSTNAME=?, CUSTOMERLASTNAME=? WHERE Movieid=?",( Movietittle , Genredescription, Viewingtimes, SEAT,STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME,  Movieid))
#     conn.commit()
#     conn.close()
# #
# #     # CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS,
# #
# #     # CUSTOMERFIRSTNAME=?, CUSTOMERLASTNAME=?, EMAIL=?, STATUS=?
# #
# def count():
#     conn=sqlite3.connect("Cinema5.db")
#     cur=conn.cursor()
#     cur.execute('SELECT COUNT(*) FROM Booking')
#     rows=cur.fetchall()
#     conn.close()
#     return rows



connect()
# insert("Batamam","Action", "2019-4-24 14:00", "A1")
#
#
#
# ", "NULL", "NULL", "NULL", "Available")

# print(search(SEAT="K1"))
# insert("Aquaman", "2019-4-24 14:00", "A1")
# print(view())
# insert("Bumblebee","Fiction",25012019)
# print(view())
#update(2,"Aquaman","Action",26012019)
#print(search(Movietittle="Bumblebee"))
# delete(10)
# print(view())
#print(count())

# update( 4,"Aquaman2","Comdedy", "2019-4-24 14:00", "A5")

# update(1,"Robbin","TTT","2019-4-24 14:00","A1","NULL", "NULL", "NULL")

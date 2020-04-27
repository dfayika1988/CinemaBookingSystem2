import sqlite3
import datetime

import sqlite3




def connect():
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS Booking (Movieid INTEGER PRIMARY KEY, Movietittle TEXT, Genredescription TEXT, Viewingtimes DATETIME, SEAT VARCHAR, STATUS TEXT, CUSTOMERFIRSTNAME TEXT, CUSTOMERLASTNAME TEXT,EMAIL VARCHAR, PRICE integer ) ")
    # EMAIL TEXT)")
    conn.commit()
    conn.close()

def connect():
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS cancelbookings (Movieid INTEGER PRIMARY KEY, Movietittle TEXT, Genredescription TEXT, Viewingtimes DATETIME, SEAT VARCHAR, STATUS TEXT, CUSTOMERFIRSTNAME TEXT, CUSTOMERLASTNAME TEXT,EMAIL VARCHAR, PRICE integer ) ")
    conn.commit()
    conn.close()



def connectbefore_delete():
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute( "CREATE TRIGGER IF NOT EXISTS prevent_deleting_bookings_from_th_epast BEFORE DELETE on Booking BEGIN SELECT CASE WHEN OLD.Viewingtimes = (SELECT Viewingtimes FROM Booking WHERE STATUS='booked' AND datetime (Viewingtimes) < datetime('now')) then RAISE(ABORT,'This a past booking it cannot be delete') END; END")
    conn.commit()
    conn.close()


def connectindex():
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("CREATE UNIQUE INDEX IF NOT EXISTS Moviecreation ON Booking (Viewingtimes , SEAT)")
    conn.commit()
    conn.close()

def prevent_double_booking():
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("CREATE TRIGGER IF NOT EXISTS  prevent_adding_booking_with_a_past_date BEFORE INSERT ON Booking BEGIN SELECT CASE when New.Viewingtimes = ( select Viewingtimes from booking where datetime ( Viewingtimes) < datetime('now')) THEN RAISE ( ABORT,'This is a past date') END; END")
    conn.commit()
    conn.close()

def email_format():
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("CREATE TRIGGER IF NOT EXISTS validate_email_before_update before update on Booking BEGIN SELECT CASE WHEN NEW.EMAIL NOT LIKE '%_@__%.__%' THEN RAISE ( ABORT, 'Invalid email address' ) END; END")
    conn.commit()
    conn.close()



def email_require():
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("CREATE TRIGGER IF NOT EXISTS email_require BEFORE UPDATE ON Booking BEGIN SELECT CASE WHEN NEW.EMAIL=''THEN RAISE(ABORT,'Email required ') END; END")
    conn.commit()
    conn.close()




def insert(Movietittle , Genredescription, Viewingtimes, SEAT,STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE):  # ,STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle  , Genredescription, Viewingtimes,'A', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) #CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle  , Genredescription, Viewingtimes,'B', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE))#,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle  , Genredescription, Viewingtimes,'C', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) #,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle  , Genredescription, Viewingtimes,'D', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)),#CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle  , Genredescription, Viewingtimes,'E', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) #,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle  , Genredescription, Viewingtimes,'F', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) #,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle  , Genredescription, Viewingtimes,'G', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) #,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle  , Genredescription, Viewingtimes,'H', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) #CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle  , Genredescription,  Viewingtimes,'I', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) #,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle  , Genredescription,  Viewingtimes,'J', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) # ,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle  , Genredescription, Viewingtimes,'K', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) # ,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription,  Viewingtimes,'L', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE))  #,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'M', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) #,CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'N', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) #CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'O', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) #CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'Q', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) # CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription,  Viewingtimes,'R', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) #CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription,  Viewingtimes,'S', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) # CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription,  Viewingtimes,'T', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) # CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    cur.execute("INSERT INTO Booking VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,'U', "available", CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE)) #CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS))
    conn.commit()
    conn.close()
    view()

def view():
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Booking")
    rows=cur.fetchall()
    conn.close()
    return rows

def viewbooked():
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Booking WHERE STATUS = 'booked' AND datetime (Viewingtimes) < datetime('now')")
    rows=cur.fetchall()
    conn.close()
    return rows

def fviewbooked():
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Booking WHERE STATUS = 'booked' AND datetime (Viewingtimes) > datetime('now')")
    rows=cur.fetchall()
    conn.close()
    return rows


def ecancelsearch(STATUS=""):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM cancelbookings WHERE STATUS='{'canceled'}' ")
    rows=cur.fetchall()
    conn.close()
    return rows




def search(Movietittle="" , Genredescription="", Viewingtimes="", SEAT="",STATUS="" ,CUSTOMERFIRSTNAME="", CUSTOMERLASTNAME="", EMAIL="", PRICE=""):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM Booking WHERE Movietittle=? OR  Genredescription=? OR Viewingtimes=? OR SEAT=?  OR STATUS=? OR CUSTOMERFIRSTNAME=? OR CUSTOMERLASTNAME=?  OR EMAIL=? OR PRICE=?",(Movietittle , Genredescription, Viewingtimes, SEAT, STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME,EMAIL, PRICE ))
    rows=cur.fetchall()
    conn.close()
    return rows

def delete(Movieid):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM Booking WHERE Movieid  =?",(Movieid,))
    conn.commit()
    conn.close()
# # #
def update(Movieid,Movietittle , Genredescription, Viewingtimes, SEAT, STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME,EMAIL, PRICE ):  ##, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("UPDATE Booking SET Movietittle=?, Genredescription=?, Viewingtimes=?, SEAT=?, STATUS=?,CUSTOMERFIRSTNAME=?, CUSTOMERLASTNAME=?, EMAIL=?, PRICE=? WHERE Movieid=?",( Movietittle , Genredescription, Viewingtimes, SEAT,STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME,EMAIL, PRICE,  Movieid))
    conn.commit()
    conn.close()


def count(Movietittle="",Viewingtimes="",STATUS=""):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute(f"SELECT COUNT(*) FROM Booking WHERE Movietittle='{Movietittle}' AND Viewingtimes='{Viewingtimes}' AND  STATUS='{STATUS}'AND datetime (Viewingtimes) > datetime('now')")
    rows=cur.fetchall()
    conn.close()
    return rows



######################################Customer booking page


def csearchtittle(Movietittle="",STATUS="",):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM Booking WHERE Movietittle='{Movietittle}' AND STATUS='{'available'}' AND datetime (Viewingtimes) > datetime('now')")
    rows=cur.fetchall()
    conn.close()
    return rows


def csearchtime(Viewingtimes="",STATUS=""):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM Booking WHERE Viewingtimes='{Viewingtimes}' AND STATUS='{'available'} AND datetime (Viewingtimes) > datetime('now')'")
    rows=cur.fetchall()
    conn.close()
    return rows


def csearchGenredes(Genredescription="",STATUS=""):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM Booking WHERE Genredescription='{Genredescription}' AND STATUS='{'available'} AND datetime (Viewingtimes) > datetime('now')'")
    rows=cur.fetchall()
    conn.close()
    return rows

def caldultupdate(Movieid,Movietittle , Genredescription, Viewingtimes, SEAT, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME,EMAIL, ):  ##, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("UPDATE Booking SET Movietittle=?, Genredescription=?, Viewingtimes=?, SEAT=?, STATUS='booked',CUSTOMERFIRSTNAME=?, CUSTOMERLASTNAME=?, EMAIL=?, PRICE=17.5 WHERE Movieid=?",( Movietittle , Genredescription, Viewingtimes, SEAT, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME,EMAIL,   Movieid))
    conn.commit()
    conn.close()



def ckidupdate(Movieid,Movietittle , Genredescription, Viewingtimes, SEAT, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME,EMAIL, ):  ##, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("UPDATE Booking SET Movietittle=?, Genredescription=?, Viewingtimes=?, SEAT=?, STATUS='booked',CUSTOMERFIRSTNAME=?, CUSTOMERLASTNAME=?, EMAIL=?, PRICE=10.5 WHERE Movieid=?",( Movietittle , Genredescription, Viewingtimes, SEAT, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME,EMAIL,   Movieid))
    conn.commit()
    conn.close()



#################history

# def hsearchtittle(Movietittle=""):
#     conn=sqlite3.connect("Cinema12.db")
#     cur=conn.cursor()
#     cur.execute("SELECT * FROM Booking WHERE Movietittle=? AND STATUS='available' ",(Movietittle))
#     rows=cur.fetchall()
#     conn.close()
#     return rows
#
# def hsearchtime(Viewingtimes="",STATUS=""):
#     conn=sqlite3.connect("Cinema12.db")
#     cur=conn.cursor()
#     cur.execute(f"SELECT * FROM Booking WHERE Viewingtimes='{Viewingtimes}' AND STATUS='{'available'}'")
#     rows=cur.fetchall()
#     conn.close()
#     return rows
#
#
# def hsearchGenredes(Genredescription="",STATUS=""):
#     conn=sqlite3.connect("Cinema12.db")
#     cur=conn.cursor()
#     cur.execute(f"SELECT * FROM Booking WHERE Genredescription='{Genredescription}' AND STATUS='{'available'}'")
#     rows=cur.fetchall()
#     conn.close()
#     return rows




# def csearchGenredes(Genredescription=""):
#     conn=sqlite3.connect("Cinema12.db")
#     cur=conn.cursor()
#     cur.execute("SELECT * FROM Booking WHERE Genredescription=? AND STATUS='Aviable'",(Genredescription))
#     rows=cur.fetchall()
#     conn.close()
#     return rows
#


#######################################################history
def haldultupdate(Movieid,Movietittle , Genredescription, Viewingtimes, SEAT, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME,EMAIL, ):  ##, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, STATUS):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("UPDATE Booking SET Movietittle=?, Genredescription=?, Viewingtimes=?, SEAT=?, STATUS='booked',CUSTOMERFIRSTNAME=?, CUSTOMERLASTNAME=?, EMAIL=?, PRICE=17.5 WHERE Movieid=?",( Movietittle , Genredescription, Viewingtimes, SEAT, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME,EMAIL,   Movieid))
    conn.commit()
    conn.close()

def cancel(Movieid,Movietittle , Genredescription, Viewingtimes, SEAT ):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("UPDATE Booking SET Movietittle=?, Genredescription=?, Viewingtimes=?, SEAT=?, STATUS='available',CUSTOMERFIRSTNAME='', CUSTOMERLASTNAME='', EMAIL='', PRICE='' WHERE Movieid=?",( Movietittle , Genredescription, Viewingtimes, SEAT, Movieid))
    conn.commit()
    conn.close()

def insertcancel (Movietittle , Genredescription, Viewingtimes, SEAT,STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO cancelbookings VALUES (NULL,?,?,?,?,?,?,?,?,?)",(Movietittle , Genredescription, Viewingtimes,SEAT, 'canceled', CUSTOMERFIRSTNAME, CUSTOMERLASTNAME, EMAIL, PRICE))
    conn.commit()
    conn.close()


# def cancelsearch(Movietittle="" , Genredescription="", Viewingtimes="", SEAT="",STATUS="" ,CUSTOMERFIRSTNAME="", CUSTOMERLASTNAME="", EMAIL="", PRICE=""):
#     conn=sqlite3.connect("Cinema12.db")
#     cur=conn.cursor()
#     cur.execute("SELECT * FROM cancelbookings WHERE Movietittle=? OR  Genredescription=? OR Viewingtimes=? OR SEAT=?  OR STATUS=? OR CUSTOMERFIRSTNAME=? OR CUSTOMERLASTNAME=?  OR EMAIL=? OR PRICE=?",(Movietittle , Genredescription, Viewingtimes, SEAT, STATUS, CUSTOMERFIRSTNAME, CUSTOMERLASTNAME,EMAIL, PRICE ))
#     rows=cur.fetchall()
#     conn.close()
#     return rows


def cancelsearch(EMAIL="",STATUS=""):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM cancelbookings WHERE EMAIL='{EMAIL}' AND STATUS='{'canceled'}' ")
    rows=cur.fetchall()
    conn.close()
    return rows



def pastsearch(EMAIL="",STATUS=""):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM Booking WHERE EMAIL='{EMAIL}' AND STATUS='{'booked'}' AND datetime (Viewingtimes) < datetime('now') ")
    rows=cur.fetchall()
    conn.close()
    return rows


def futuresearch(EMAIL="",STATUS=""):
    conn=sqlite3.connect("Cinema12.db")
    cur=conn.cursor()
    cur.execute(f"SELECT * FROM Booking WHERE EMAIL='{EMAIL}' AND STATUS='{'booked'}' AND datetime (Viewingtimes) > datetime('now') ")
    rows=cur.fetchall()
    conn.close()
    return rows



email_require()
email_format()
prevent_double_booking()
connectbefore_delete()
connectindex()
connect()

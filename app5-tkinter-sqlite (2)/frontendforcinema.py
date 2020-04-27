from tkinter import *
import cinemabackend
import tkinter.messagebox

def save_info():
    list_info = cinemabackend.view()
    list_info = str(list_info)
    print(list_info)

    file = open("For employee.The whole list", "w")
    file.write(list_info)

    file.close()
    print(" employee ",list_info, "The has been saved successfully")



def text_file_of_booked_seats():
    list_info2 = cinemabackend.viewbooked()
    list_info2 = str(list_info2)
    print(list_info2)

    file = open("For employee.The text file of booked seats in the past", "w")
    file.write(list_info2)

    file.close()
    print(" employee ",list_info2, "The has been saved successfully")


def ftext_file_of_booked_seats():
    list_info3 = cinemabackend.fviewbooked()
    list_info3 = str(list_info3)
    print(list_info3)

    file = open("For employee.The text file of booked seats in the future", "w")
    file.write(list_info3)

    file.close()
    print(" employee ",list_info3, "The has been saved successfully")

def text_file_of_available_seats():
    list_info4 = cinemabackend.search(EMovietitle_text.get(),EGenredescription_text.get(),EViewingtimes_text.get(),ESEAT_text.get(),
    ESTATUS_text.get(),ECUSTOMERFIRSTNAME_text.get(),ECUSTOMERLASTNAME_text.get(),EEMAIL_text.get(),EPRICE_text.get())
    list_info4 = str(list_info4)
    print(list_info4)

    file = open("For employee.The text file of available seats", "w")
    file.write(list_info4)

    file.close()
    print(" employee ",list_info4, "The has been saved successfully")



def raise_frame(frame):
    frame.tkraise()


def Eselectedfilmrow(event):
    global selected_tuple
    index=el1.curselection()[0]
    selected_tuple=el1.get(index)
    ee1.delete(0,END)
    ee1.insert(END,selected_tuple[1])
    ee2.delete(0,END)
    ee2.insert(END,selected_tuple[2])
    ee3.delete(0,END)
    ee3.insert(END,selected_tuple[3])
    ee4.delete(0,END)
    ee4.insert(END,selected_tuple[4])
    ee5.delete(0,END)
    ee5.insert(END,selected_tuple[5])
    ee6.delete(0,END)
    ee6.insert(END,selected_tuple[6])
    ee7.delete(0,END)
    ee7.insert(END,selected_tuple[7])
    ee8.delete(0,END)
    ee8.insert(END,selected_tuple[8])
    ee9.delete(0,END)
    ee9.insert(END,selected_tuple[9])



def view_command():
    el1.delete(0,END)
    for row in cinemabackend.view():
        el1.insert(END,row)

def view_bookedlist_command():
    el1.delete(0,END)
    for row in cinemabackend.viewbooked():
            el1.insert(END,row)

def fview_bookedlist_command():
    el1.delete(0,END)
    for row in cinemabackend.fviewbooked():
        el1.insert(END,row)

def ecancelsearch_command():
    el1.delete(0,END)
    for row in cinemabackend.ecancelsearch():
        el1.insert(END,row)

def searchmoview_command():
    el1.delete(0,END)
    for row in cinemabackend.search(EMovietitle_text.get(),EGenredescription_text.get(),EViewingtimes_text.get(),ESEAT_text.get(),ESTATUS_text.get(),ECUSTOMERFIRSTNAME_text.get(),ECUSTOMERLASTNAME_text.get(),EEMAIL_text.get(),EPRICE_text.get()):
        el1.insert(END,row)

def addmovietothelist_command():
    cinemabackend.insert(EMovietitle_text.get(),EGenredescription_text.get(),EViewingtimes_text.get(),ESEAT_text.get(),ESTATUS_text.get(),ECUSTOMERFIRSTNAME_text.get(),ECUSTOMERLASTNAME_text.get(),EEMAIL_text.get(),EPRICE_text.get())
    el1.delete(0,END)
    el1.insert(END,(EMovietitle_text.get(),EGenredescription_text.get(),EViewingtimes_text.get(),ESEAT_text.get(),ESTATUS_text.get(),ECUSTOMERFIRSTNAME_text.get(),ECUSTOMERLASTNAME_text.get(),EEMAIL_text.get(),EPRICE_text.get()))



    if addmovietothelist_command:
       employee1 = tkinter.messagebox.showinfo('Booking cinema', 'The has being added ')
    else:
        employee2 = tkinter.messagebox.showinfo('Booking cinema', 'This is an error')


def delete_command():
    cinemabackend.delete(selected_tuple[0])


    if delete_command :
        employee1 =  tkinter.messagebox.showinfo('Booking cinema', 'The booking has been deleted  ')


    if not cinemabackend.connectbefore_delete:
        employee4 = tkinter.messagebox.showinfo('Booking cinema', 'This a past booking it cannot be deleted ')



def Updatescreeninglist():
    cinemabackend.update(selected_tuple[0],EMovietitle_text.get(),EGenredescription_text.get(),EViewingtimes_text.get(),ESEAT_text.get(),ESTATUS_text.get(),ECUSTOMERFIRSTNAME_text.get(),ECUSTOMERLASTNAME_text.get(),EEMAIL_text.get(),EPRICE_text.get())


def count():
    el2.delete(0,END)
    for row in cinemabackend.count(EMovietitle_text.get(),EViewingtimes_text.get(),ESTATUS_text.get()):
        el2.insert(END,row)

window =Tk()
window.geometry("2600x1600")
window.wm_title("Cinema booking system")

Home= Frame(window)
Password_employee= Frame(window)
PageOne=Frame(window)
Customerpagea1=Frame(window)
Customerpage=Frame(window)
PageThree=Frame(window)
BookingHistorypage=Frame(window)

for frame  in (Home, Password_employee,  PageOne,Customerpagea1,Customerpage,PageThree, BookingHistorypage):
    frame.grid(row=0,column=0, sticky='news')

e1=Label(Home,text='Home')
e1.pack()
b1=Button(Home, text='Employee window',height=15,width=15, command=lambda:raise_frame(Password_employee)).pack()
s9=Button(Home, text= 'Customers window',height=15,width=15, command=lambda:raise_frame(Password_employee)).pack()


#####passowrd

pl1= Label(Password_employee, text = 'User:')
pl1.pack()
pl2= Label(Password_employee, text = 'Passowrd:')
pl2.pack()

pt1 = Entry(Password_employee, textvariable = StringVar())
pt1.pack()
pt2= Entry(Password_employee, show= '*', textvariable= StringVar())
pt2.pack()



def valid():
    u=pt1.get()
    p=pt2.get()
    if (u=='admim') and (p == 'admim'):
        pb2 = Button(Password_employee, text="""
    successful 
    employee 
  logging please click 
    here to enter""",height=15,width=15, command=lambda:raise_frame(PageOne)).pack()
    elif (u=='cust') and (p == 'cust'):
        pb3=Button(Password_employee, text= """
     successful 
     customer 
  logging please click 
     here to enter""",height=15,width=15, command=lambda:raise_frame(Customerpagea1)).pack()
    else:
        ela1 = Label(Password_employee,text="incorrect password or username ").pack()
        pb3  = Button(Password_employee, text = 'Exit',command=window.destroy).pack()

    pt1.delete(0,END)
    pt2.delete(0,END)


pb1 = Button(Password_employee, text = 'Log in', command = valid)
pb1.pack()



e4=Label(Customerpagea1,text='Customer home page')
e4.pack()
s11=Button(Customerpagea1, text='Booking History',height=15,width=15, command=lambda:raise_frame(BookingHistorypage)).pack()
bs10=Button(Customerpagea1, text='Make a  booking',height=15,width=15, command=lambda:raise_frame(Customerpage)).pack()
et10=Button(Customerpagea1, text='Log out',height=10,width=15,command=window.destroy).pack()


####The employeee part of the system
ela10=Label(PageOne,text='Employee window').grid(row=0,column=3)


ela1=Label(PageOne,text="Movie title")
ela1.grid(row=5,column=1)

ela2=Label(PageOne,text="Genre/description")
ela2.grid(row=5,column=3)

ela3=Label(PageOne,text="Viewing times")
ela3.grid(row=6,column=1)

ela4=Label(PageOne,text="Number available or booked")
ela4.grid(row=6,column=3)


ela5=Label(PageOne,text="customer first name")
ela5.grid(row=5,column=7)

ela6=Label(PageOne,text="customer last name")
ela6.grid(row=6,column=7)


ela7=Label(PageOne,text="customer email")
ela7.grid(row=7,column=7)

ela7=Label(PageOne,text="SEAT")
ela7.grid(row=8,column=7)


ela7=Label(PageOne,text="STATUS")
ela7.grid(row=9,column=7)


ela7=Label(PageOne,text="PRICE")
ela7.grid(row=10,column=7)

####These are entry


EMovietitle_text=StringVar()
ee1=Entry(PageOne,textvariable=EMovietitle_text)
ee1.grid(row=5,column=2)

EGenredescription_text=StringVar()
ee2=Entry(PageOne,textvariable=EGenredescription_text)
ee2.grid(row=5,column=4)

EViewingtimes_text=StringVar()
ee3=Entry(PageOne,textvariable=EViewingtimes_text)
ee3.grid(row=6,column=2)


ESEAT_text=StringVar()
ee4=Entry(PageOne,textvariable=ESEAT_text)
ee4.grid(row=8,column=8)

ESTATUS_text=StringVar()
ee5=Entry(PageOne,textvariable=ESTATUS_text)
ee5.grid(row=9,column=8)

ECUSTOMERFIRSTNAME_text=StringVar()
ee6=Entry(PageOne,textvariable=ECUSTOMERFIRSTNAME_text)
ee6.grid(row=5,column=8)

ECUSTOMERLASTNAME_text=StringVar()
ee7=Entry(PageOne,textvariable=ECUSTOMERLASTNAME_text)
ee7.grid(row=6,column=8)

EEMAIL_text=StringVar()
ee8=Entry(PageOne,textvariable=EEMAIL_text)
ee8.grid(row=7,column=8)

EPRICE_text=StringVar()
ee9=Entry(PageOne,textvariable=EPRICE_text)
ee9.grid(row=10,column=8)


#####################

el1=Listbox(PageOne, height=30,width=50)
el1.grid(row=7,column=1,rowspan=6,columnspan=2)

esb1=Scrollbar(PageOne)
esb1.grid(row=7,column=3,rowspan=6)
# #
el1.configure(yscrollcommand=esb1.set)
esb1.configure(command=el1.yview)

el1.bind('<<ListboxSelect>>',Eselectedfilmrow)

####count display

el2=Listbox(PageOne, height=1, width=20)
el2.grid(row=6,column=4)



############################

eb1=Button(PageOne,text="View movies list", width=16, command=view_command)
eb1.grid(row=7,column=4)
#
eb2=Button(PageOne,text="Search for movies", width=16, command= searchmoview_command)
eb2.grid(row=8,column=4)

eb3=Button(PageOne,text="Add a movie", width=16 ,command= addmovietothelist_command)
eb3.grid(row=9,column=4)

eb4=Button(PageOne,text="Update screening list", width=16, command=Updatescreeninglist)
eb4.grid(row=10,column=4)

eb5=Button(PageOne,text="Delete", width=16, command=delete_command)
eb5.grid(row=11,column=4)

eb6=Button(PageOne,text="Close", width=16, command=window.destroy)
eb6.grid(row=12,column=4)


eb7=Button(PageOne,text="Number available or booked", width=22,command=count)
eb7.grid(row=13,column=4)


eb8=Button(PageOne,text="Text of the whole list ", width=20, command=save_info)
eb8.grid(row=15,column=4)


eb9=Button(PageOne,text="List of booked seats in the past  ", width=26, command=view_bookedlist_command)
eb9.grid(row=16,column=4)

eb10=Button(PageOne,text="Text file of booked seats in the past  ", width=26, command=text_file_of_booked_seats)
eb10.grid(row=17,column=4)


eb11=Button(PageOne,text="List of booked seats in the future", width=26, command=fview_bookedlist_command)
eb11.grid(row=11,column=8)


eb12=Button(PageOne,text="Text file of booked seats in the future", width=26, command=ftext_file_of_booked_seats)
eb12.grid(row=12,column=8)

eb13=Button(PageOne,text="Text file of available seats", width=26, command=text_file_of_available_seats)
eb13.grid(row=13,column=8)



eb14=Button(PageOne,text="search cancellation list", width=20, command=ecancelsearch_command)
eb14.grid(row=14,column=8)



def clear2():
    pt1.delete(0,END)
    pt2.delete(0,END)
    raise_frame(Home)
    window.destroy()


eb11=Button(PageOne, text='Log out', command=clear2).grid(row=15,column=8)


# ###############################################################################The Customer part of the system

def Cselectedfilmrow(event):
    global Cselected_tuple
    index=cl1.curselection()[0]
    Cselected_tuple=cl1.get(index)
    ce1.delete(0,END)
    ce1.insert(END,Cselected_tuple[1])
    ce2.delete(0,END)
    ce2.insert(END,Cselected_tuple[2])
    ce3.delete(0,END)
    ce3.insert(END,Cselected_tuple[3])
    ce4.delete(0,END)
    ce4.insert(END,Cselected_tuple[4])
    ce5.delete(0,END)
    ce5.insert(END,Cselected_tuple[5])
    ce6.delete(0,END)
    ce6.insert(END,Cselected_tuple[6])
    ce7.delete(0,END)
    ce7.insert(END,Cselected_tuple[7])
    ce8.delete(0,END)
    ce8.insert(END,Cselected_tuple[8])
    ce9.delete(0,END)
    ce9.insert(END,Cselected_tuple[9])


def csearchmoview_command():
    cl1.delete(0,END)
    for row in cinemabackend.csearchtittle(CMovietitle_text.get()):
        cl1.insert(END,row)

def csearchmoview2_command():
    cl1.delete(0,END)
    for row in cinemabackend.csearchtime(CViewingtimes_text.get()):
        cl1.insert(END,row)

def csearchmoview3_command():
    cl1.delete(0,END)
    for row in cinemabackend.csearchGenredes(CGenredescription_text.get()):
        cl1.insert(END,row)


def cUpdatescreeninglist():
    cl1.delete(0,END)
    cinemabackend.caldultupdate(Cselected_tuple[0],CMovietitle_text.get(),CGenredescription_text.get(),CViewingtimes_text.get(),CSEAT_text.get(),CCUSTOMERFIRSTNAME_text.get(),CCUSTOMERLASTNAME_text.get(),CEMAIL_text.get())
    raise_frame(Customerpagea1)
    tkinter.messagebox.showinfo('Customer cinema', 'This booking has been confirmed')
    ce1.delete(0,END)
    ce2.delete(0,END)
    ce3.delete(0,END)
    ce4.delete(0,END)
    ce5.delete(0,END)
    ce6.delete(0,END)
    ce7.delete(0,END)
    ce8.delete(0,END)
    ce9.delete(0,END)






def cKUpdatescreeninglist():
    cl1.delete(0,END)
    cinemabackend.ckidupdate(Cselected_tuple[0],CMovietitle_text.get(),CGenredescription_text.get(),CViewingtimes_text.get(),CSEAT_text.get(),CCUSTOMERFIRSTNAME_text.get(),CCUSTOMERLASTNAME_text.get(),CEMAIL_text.get())
    raise_frame(Customerpagea1)
    tkinter.messagebox.showinfo('Customer cinema', 'This booking has been confirmed')
    ce1.delete(0,END)
    ce2.delete(0,END)
    ce3.delete(0,END)
    ce4.delete(0,END)
    ce5.delete(0,END)
    ce6.delete(0,END)
    ce7.delete(0,END)
    ce8.delete(0,END)
    ce9.delete(0,END)


cla10=Label(Customerpage,text='Customer booking window').grid(row=0,column=3)


cla1=Label(Customerpage,text="Movie title")
cla1.grid(row=5,column=1)

cla2=Label(Customerpage,text="Genre/description")
cla2.grid(row=5,column=3)

cla3=Label(Customerpage,text="Viewing times")
cla3.grid(row=6,column=1)

cla5=Label(Customerpage,text="customer first name")
cla5.grid(row=5,column=7)

cla6=Label(Customerpage,text="customer last name")
cla6.grid(row=6,column=7)


cla8=Label(Customerpage,text="customer email")
cla8.grid(row=7,column=7)

cla9=Label(Customerpage,text="SEAT")
cla9.grid(row=8,column=7)


cla13=Label(Customerpage,text="STATUS")
cla13.grid(row=9,column=7)


cla11=Label(Customerpage,text="""
In order for the booking 
To be confirmed 
an email in the correct format
first name 
last name 
is required.
""")
cla11.grid(row=10,column=8)

####These are entry

CMovietitle_text=StringVar()
ce1=Entry(Customerpage,textvariable=CMovietitle_text)
ce1.grid(row=5,column=2)

CGenredescription_text=StringVar()
ce2=Entry(Customerpage,textvariable=CGenredescription_text)
ce2.grid(row=5,column=4)

CViewingtimes_text=StringVar()
ce3=Entry(Customerpage,textvariable=CViewingtimes_text)
ce3.grid(row=6,column=2)


CSEAT_text=StringVar()
ce4=Entry(Customerpage,textvariable=CSEAT_text)
ce4.grid(row=8,column=8)

CSTATUS_text=StringVar()
ce5=Entry(Customerpage,textvariable=CSTATUS_text)
ce5.grid(row=9,column=8)

CCUSTOMERFIRSTNAME_text=StringVar()
ce6=Entry(Customerpage,textvariable=CCUSTOMERFIRSTNAME_text)
ce6.grid(row=5,column=8)

CCUSTOMERLASTNAME_text=StringVar()
ce7=Entry(Customerpage,textvariable=CCUSTOMERLASTNAME_text)
ce7.grid(row=6,column=8)

CEMAIL_text=StringVar()
ce8=Entry(Customerpage,textvariable=CEMAIL_text)
ce8.grid(row=7,column=8)

CPRICE_text=StringVar()
ce9=Entry(Customerpage,textvariable=CPRICE_text)
# ce9.grid(row=10,column=8)


#####################

cl1=Listbox(Customerpage, height=30,width=50)
cl1.grid(row=7,column=1,rowspan=6,columnspan=2)

csb1=Scrollbar(Customerpage)
csb1.grid(row=7,column=3,rowspan=6)
# #
cl1.configure(yscrollcommand=csb1.set)
csb1.configure(command=cl1.yview)

cl1.bind('<<ListboxSelect>>',Cselectedfilmrow)



############################

cb1=Button(Customerpage,text="Search by time and date", width=20, command=csearchmoview2_command)
cb1.grid(row=7,column=4)
#
cb2=Button(Customerpage,text="Search by title", width=20, command= csearchmoview_command)
cb2.grid(row=8,column=4)

cb3=Button(Customerpage,text="Search by genre", width=20 ,command= csearchmoview3_command)
cb3.grid(row=9,column=4)

cb4=Button(Customerpage,text="Confirm your booking adult price is 17.50 ", width=30, command=cUpdatescreeninglist)
cb4.grid(row=10,column=4)

cb5=Button(Customerpage,text="Confirm your booking kids price is 10.50", width=30, command=cKUpdatescreeninglist)
cb5.grid(row=11,column=4)

cb6=Button(Customerpage,text="Close", width=16, command=window.destroy)
cb6.grid(row=12,column=4)


cb10=Button(Customerpage, text='BookingHistorypage', command=lambda:raise_frame(BookingHistorypage)).grid(row=13,column=7)

cb11=Button(Customerpage, text='Customer home page', command=lambda:raise_frame(Customerpagea1)).grid(row=13,column=8)


##################Customer History page
def Hselectedfilmrow(event):
    global Hselected_tuple
    index=hl1.curselection()[0]
    Hselected_tuple=hl1.get(index)
    he1.delete(0,END)
    he1.insert(END,Hselected_tuple[1])
    he2.delete(0,END)
    he2.insert(END,Hselected_tuple[2])
    he3.delete(0,END)
    he3.insert(END,Hselected_tuple[3])
    he4.delete(0,END)
    he4.insert(END,Hselected_tuple[4])
    he5.delete(0,END)
    he5.insert(END,Hselected_tuple[5])
    he6.delete(0,END)
    he6.insert(END,Hselected_tuple[6])
    he7.delete(0,END)
    he7.insert(END,Hselected_tuple[7])
    he8.delete(0,END)
    he8.insert(END,Hselected_tuple[8])
    he9.delete(0,END)
    he9.insert(END,Hselected_tuple[9])

def hview_command():
    hl1.delete(0,END)
    for row in cinemabackend.view():
        hl1.insert(END,row)

def searchcancelbooking_command():
    hl1.delete(0,END)
    for row in cinemabackend.cancelsearch(HEMAIL_text.get()):
        hl1.insert(END,row)


def futuresearch_command():
    hl1.delete(0,END)
    for row in cinemabackend.futuresearch(HEMAIL_text.get()):
        hl1.insert(END,row)

    he9.delete(0,END)

def pastsearch_command():
    hl1.delete(0,END)
    for row in cinemabackend.pastsearch(HEMAIL_text.get()):
        hl1.insert(END,row)


def cancel_list():

    cinemabackend.cancel(Hselected_tuple[0],HMovietitle_text.get(),HGenredescription_text.get(),HViewingtimes_text.get(),HSEAT_text.get())
    cinemabackend.insertcancel(HMovietitle_text.get(),HGenredescription_text.get(),HViewingtimes_text.get(),HSEAT_text.get(),HSTATUS_text.get(),HCUSTOMERFIRSTNAME_text.get(),HCUSTOMERLASTNAME_text.get(),HEMAIL_text.get(),HPRICE_text.get())
    hl1.delete(0,END)
    tkinter.messagebox.showinfo('Customer cinema', 'The booking has canceled ')

def clear_screen():
    hl1.delete(0,END)
    he8.delete(0,END)
    raise_frame(Customerpagea1)

def clear_screen2():
    hl1.delete(0,END)
    he8.delete(0,END)
    raise_frame(Customerpage)




# def hKUpdatescreeninglist():
#     cinemabackend.hkidupdate(Hselected_tuple[0],HMovietitle_text.get(),HGenredescription_text.get(),HViewingtimes_text.get(),HSEAT_text.get(),HCUSTOMERFIRSTNAME_text.get(),HCUSTOMERLASTNAME_text.get(),HEMAIL_text.get())
#
#

hla10=Label(BookingHistorypage,text='Customer booking history window').grid(row=0,column=3)


#
hla8=Label(BookingHistorypage,text="Enter your email")
hla8.grid(row=5,column=1)



####These are entry

HMovietitle_text=StringVar()
he1=Entry(BookingHistorypage,textvariable=HMovietitle_text)
# he1.grid(row=5,column=2)

HGenredescription_text=StringVar()
he2=Entry(BookingHistorypage,textvariable=HGenredescription_text)
# he2.grid(row=5,column=4)
#
HViewingtimes_text=StringVar()
he3=Entry(BookingHistorypage,textvariable=HViewingtimes_text)
# he3.grid(row=6,column=2)
#
#
HSEAT_text=StringVar()
he4=Entry(BookingHistorypage,textvariable=HSEAT_text)
# he4.grid(row=8,column=8)
#
HSTATUS_text=StringVar()
he5=Entry(BookingHistorypage,textvariable=HSTATUS_text)
# he5.grid(row=9,column=8)
#
HCUSTOMERFIRSTNAME_text=StringVar()
he6=Entry(BookingHistorypage,textvariable=HCUSTOMERFIRSTNAME_text)
# he6.grid(row=5,column=8)
#
HCUSTOMERLASTNAME_text=StringVar()
he7=Entry(BookingHistorypage,textvariable=HCUSTOMERLASTNAME_text)
# he7.grid(row=6,column=8)

HEMAIL_text=StringVar()
he8=Entry(BookingHistorypage,textvariable=HEMAIL_text)
he8.grid(row=5,column=2)

HPRICE_text=StringVar()
he9=Entry(BookingHistorypage,textvariable=HPRICE_text)
# he9.grid(row=10,column=8)


#####################

hl1=Listbox(BookingHistorypage, height=30,width=50)
hl1.grid(row=7,column=1,rowspan=6,columnspan=2)

hsb1=Scrollbar(BookingHistorypage)
hsb1.grid(row=7,column=3,rowspan=6)
# #
hl1.configure(yscrollcommand=hsb1.set)
hsb1.configure(command=hl1.yview)

hl1.bind('<<ListboxSelect>>',Hselectedfilmrow)



############################

hb1=Button(BookingHistorypage,text="Search canceled bookings", width=20, command=searchcancelbooking_command)
hb1.grid(row=7,column=4)
#
hb2=Button(BookingHistorypage,text=" Search past booking ", width=20, command=pastsearch_command)
hb2.grid(row=8,column=4)

hb3=Button(BookingHistorypage,text="Search future booking", width=20 ,command=futuresearch_command)
hb3.grid(row=9,column=4)

hb4=Button(BookingHistorypage,text="Cancel ", width=25, command=cancel_list)
hb4.grid(row=10,column=4)

hb6=Button(BookingHistorypage,text="Close", width=16, command=window.destroy)
hb6.grid(row=12,column=4)

hb1=Button(BookingHistorypage,text="Make a booking page", width=16,  command=clear_screen2)
hb1.grid(row=13,column=4)

# hb1=Button(BookingHistorypage,text="Make a booking page", width=16, command=lambda:raise_frame(Customerpage))
# hb1.grid(row=13,column=4)


hb10=Button(BookingHistorypage, text='Customer home page', command=clear_screen).grid(row=13,column=7)

# hb11=Button(BookingHistorypage, text='Go to Home', command=clear_screen).grid(row=13,column=8)



raise_frame(Home)

window.mainloop()
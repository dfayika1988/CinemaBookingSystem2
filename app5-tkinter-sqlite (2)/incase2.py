from tkinter import *
import cinemabackend

def raise_frame(frame):
    frame.tkraise()


def selectedfilmrow(event):
    global selected_tuple
    index=el1.curselection()[0]
    selected_tuple=el1.get(index)
    ee1.delete(0,END)
    ee1.insert(END,selected_tuple[1])
    ee2.delete(0,END)
    ee2.insert(END,selected_tuple[2])
    ee3.delete(0,END)
    ee3.insert(END,selected_tuple[3])

#
def view_command():
    el1.delete(0,END)###This ensure I am deleting if press the buttom
    for row in cinemabackend.view():
        el1.insert(END,row)###The rows will put at the of the list box

def searchmoview_command():
    el1.delete(0,END)
    for row in cinemabackend.search(EMovietitle_text.get(),EGenredescription_text.get(),EViewingtimes_text.get(),ESEAT_text.get(),ESTATUS_text.get(),ECUSTOMERFIRSTNAME_text.get(),ECUSTOMERLASTNAME_text.get()): #EEMAIL_text.get(),ECUSTOMERFIRSTNAME_text.get(),ECUSTOMERLASTNAME_text.get(),EEMAIL_text.get()):
        el1.insert(END,row)

def addmovietothelist_command():
    cinemabackend.insert(EMovietitle_text.get(),EGenredescription_text.get(),EViewingtimes_text.get(),ESEAT_text.get(),ESTATUS_text.get(),ECUSTOMERFIRSTNAME_text.get(),ECUSTOMERLASTNAME_text.get())#,ESTATUS_text.get(),CUSTOMERFIRSTNAME_text.get(),CUSTOMERLASTNAME_text.get(),EMAIL_text.get,STATUS_text.get())
    el1.delete(0,END)
    el1.insert(END,(EMovietitle_text.get(),EGenredescription_text.get(),EViewingtimes_text.get(),ESEAT_text.get(),ESTATUS_text.get(),ECUSTOMERFIRSTNAME_text.get(),ECUSTOMERLASTNAME_text.get())) #,CUSTOMERFIRSTNAME_text.get(),CUSTOMERLASTNAME_text.get(),EMAIL_text.get,STATUS_text.get())) ###add the film in a single line


def delete_command():
    cinemabackend.delete(selected_tuple[0])

def Updatescreeninglist():
    cinemabackend.update(selected_tuple[0],EMovietitle_text.get(),EGenredescription_text.get(),EViewingtimes_text.get(),ESEAT_text.get(),ESTATUS_text.get(),ECUSTOMERFIRSTNAME_text.get(),ECUSTOMERLASTNAME_text.get())


def count():
    el1.delete(0,END)###This ensure I am deleting if press the buttom
    for row in cinemabackend.count():
        el1.insert(END,row)###The rows will put at the of the list box

window =Tk()
window.geometry("2600x1600")
window.wm_title("Employee Cinema booking system")

Home= Frame(window)
PageOne=Frame(window)
Customerpagea1=Frame(window)
Customerpage=Frame(window)
PageThree=Frame(window)
BookingHistorypage=Frame(window)

for frame  in (Home, PageOne,Customerpagea1,Customerpage,PageThree, BookingHistorypage):
    frame.grid(row=0,column=0, sticky='news')

e1=Label(Home,text='Home')
e1.pack()
s1=Button(Home, text='Employee window',height=15,width=15, command=lambda:raise_frame(PageOne)).pack()
s9=Button(Home, text= 'Customers window',height=15,width=15, command=lambda:raise_frame(Customerpagea1)).pack()

e4=Label(Customerpagea1,text='Home')
e4.pack()
s11=Button(Customerpagea1, text='Booking History',height=15,width=15, command=lambda:raise_frame(BookingHistorypage)).pack()
s10=Button(Customerpagea1, text='Make a  booking',height=15,width=15, command=lambda:raise_frame(Customerpage)).pack()


####The employeee part of the system
ela10=Label(PageOne,text='Employee window').grid(row=0,column=3)


ela1=Label(PageOne,text="Movie title")
ela1.grid(row=5,column=1)

ela2=Label(PageOne,text="Genre/description")
ela2.grid(row=5,column=3)

ela3=Label(PageOne,text="Viewing times")
ela3.grid(row=6,column=1)

ela4=Label(PageOne,text="Count")
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

# Viewingtimes_text=StringVar()
# ee4=Entry(PageOne,textvariable=Viewingtimes_text)
# ee4.grid(row=6,column=4)

ECUSTOMERFIRSTNAME_text=StringVar()
ee5=Entry(PageOne,textvariable=ECUSTOMERFIRSTNAME_text)
ee5.grid(row=5,column=8)


ECUSTOMERLASTNAME_text=StringVar()
ee6=Entry(PageOne,textvariable=ECUSTOMERLASTNAME_text)
ee6.grid(row=6,column=8)

EEMAIL_text=StringVar()
ee7=Entry(PageOne,textvariable=EEMAIL_text)
ee7.grid(row=7,column=8)

ESEAT_text=StringVar()
ee7=Entry(PageOne,textvariable=ESEAT_text)
ee7.grid(row=8,column=8)

ESTATUS_text=StringVar()
ee7=Entry(PageOne,textvariable=ESTATUS_text)
ee7.grid(row=9,column=8)

#####################

el1=Listbox(PageOne, height=30,width=50)
el1.grid(row=7,column=1,rowspan=6,columnspan=2)

esb1=Scrollbar(PageOne)
esb1.grid(row=7,column=3,rowspan=6)
# #
el1.configure(yscrollcommand=esb1.set)
esb1.configure(command=el1.yview)

el1.bind('<<ListboxSelect>>',selectedfilmrow)

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


eb7=Button(PageOne,text="Count", width=16,command=count)
eb7.grid(row=13,column=4)


eb8=Button(PageOne,text="Delete customer info", width=16)    #,command=count)
eb8.grid(row=15,column=4)


eb9=Button(PageOne,text="Update customer info", width=16)    #,command=count)
eb9.grid(row=17,column=4)

# b6=Button(PageOne,text="Close", width=16,command=window.destroy)
# b6.grid(row=1,column=7)
# Label(PageOne,text='Home').grid(row=0,column=8)






eb10=Button(PageOne, text='Go to page3', command=lambda:raise_frame(PageThree)).grid(row=13,column=7)

eb11=Button(PageOne, text='Go to Home', command=lambda:raise_frame(Home)).grid(row=13,column=8)

#
# ###############################################################################The Customer part of the system
# Label(Customerpage,text='customer window').grid(row=0,column=3)
# s4=Button(Customerpage, text='Go to page4', command=lambda:raise_frame(BookingHistorypage)).grid(row=0,column=5)
#
#
#
# l1=Label(Customerpage,text="Movie title")
# l1.grid(row=5,column=1)
#
# l2=Label(Customerpage,text="Genre/description")
# l2.grid(row=5,column=3)
#
# l3=Label(Customerpage,text="Viewing times")
# l3.grid(row=6,column=1)
#
# l4=Label(Customerpage,text="Enter email")
# l4.grid(row=6,column=3)
#
#
# l5=Label(Customerpage,text="Enter first name")
# l5.grid(row=5,column=7)
#
# l6=Label(Customerpage,text="Enter last name")
# l6.grid(row=6,column=7)
#
#
# l7=Label(Customerpage,height=20,width=24, text='''Instructions
# (1) Please search for the movie
# (2) Select time,seat and Movie
# (3) Click price
# (4) Enter your details
# (5) Click Book''')
# l7.grid(row=7,column=7)
#
# ####These are entry
#
# Movietitle_text=StringVar()
# e1=Entry(Customerpage,textvariable=Movietitle_text)
# e1.grid(row=5,column=2)
#
# Genredescription_text=StringVar()
# e2=Entry(Customerpage,textvariable=Genredescription_text)
# e2.grid(row=5,column=4)
#
# Viewingtimes_text=StringVar()
# e3=Entry(Customerpage,textvariable=Viewingtimes_text)
# e3.grid(row=6,column=2)
#
# Customeremail_text=StringVar()
# e3=Entry(Customerpage,textvariable=Customeremail_text)
# e3.grid(row=6,column=4)
#
# CustomerfirstName_text=StringVar()
# e1=Entry(Customerpage,textvariable=CustomerfirstName_text)
# e1.grid(row=5,column=8)
#
#
# CustomerlastName_text=StringVar()
# e1=Entry(Customerpage,textvariable=CustomerlastName_text)
# e1.grid(row=6,column=8)
#
# # Customeremail_text=StringVar()
# # e1=Entry(Customerpage,textvariable=Customeremail_text)
# # e1.grid(row=7,column=8)
#
#
# #####################
#
# list1=Listbox(Customerpage, height=30,width=50)
# list1.grid(row=7,column=1,rowspan=6,columnspan=2)
#
# sb1=Scrollbar(Customerpage)
# sb1.grid(row=7,column=3,rowspan=6)
# # #
# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=list1.yview)
#
# # list1.bind('<<ListboxSelect>>',selectedfilmrow)
#
# b1=Button(Customerpage,text="Search for movies", width=16) #,  command=view_command)
# b1.grid(row=7,column=4)
# #
# b2=Button(Customerpage,text="Book a movie", width=16)  #, command= searchmoview_command)
# b2.grid(row=8,column=4)
#
# check1=Checkbutton(Customerpage,text="£17.5 for Adults", width=16)  #   ,command= addmovietothelist_command)
# check1.grid(row=9,column=4)
#
# check1=Checkbutton(Customerpage,text="£10 for Kids", width=16)  #   ,command= addmovietothelist_command)
# check1.grid(row=10,column=4)
#
#
# s7=Button(Customerpage, text='BookingHistorypage', command=lambda:raise_frame(BookingHistorypage)).grid(row=13,column=7)
#
# s8=Button(Customerpage, text='Go to Home', command=lambda:raise_frame(Home)).grid(row=13,column=8)
#
#
# ######Last of the interface
#
#
# Label(PageThree,text='Go to page3').pack()
# s5=Button(PageThree, text='Go to Home', command=lambda:raise_frame(Home)).pack()
#
#
#
#
#
#
#
#
#
#
#
#
# ###############################################Customer booking history
# Label(BookingHistorypage,text='Booking History page').grid(row=0,column=3)
# s6=Button(BookingHistorypage, text='Go to Home', command=lambda:raise_frame(Home)).grid(row=0,column=4)
#
#
#
# l1=Label(BookingHistorypage,text="Enter your email addres")
# l1.grid(row=5,column=1)
#
#
# ####These are entry
#
# Enteryouremailaddres_text=StringVar()
# e1=Entry(BookingHistorypage,textvariable=Enteryouremailaddres_text)
# e1.grid(row=5,column=2)
#
#
#
# #####################
#
# list1=Listbox(BookingHistorypage, height=30,width=50)
# list1.grid(row=7,column=1,rowspan=6,columnspan=2)
#
# sb1=Scrollbar(BookingHistorypage)
# sb1.grid(row=7,column=3,rowspan=6)
# # #
# list1.configure(yscrollcommand=sb1.set)
# sb1.configure(command=list1.yview)
#
# # list1.bind('<<ListboxSelect>>',selectedfilmrow)
#
# b1=Button(BookingHistorypage,text="Search for booking", width=16) #,  command=view_command)
# b1.grid(row=7,column=4)
# #
# b2=Button(BookingHistorypage,text="Cancel booking", width=16)  #, command= searchmoview_command)
# b2.grid(row=8,column=4)
#
# b3=Button(BookingHistorypage,text="Update your details", width=16)  #   ,command= addmovietothelist_command)
# b3.grid(row=9,column=4)
#
#
# s2=Button(BookingHistorypage, text='Go to page3', command=lambda:raise_frame(PageThree)).grid(row=13,column=7)
#
# s3=Button(BookingHistorypage, text='Go to Home', command=lambda:raise_frame(Home)).grid(row=13,column=8)


raise_frame(Home)

window.mainloop()
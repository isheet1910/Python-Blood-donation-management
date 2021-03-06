from tkinter import *
import tkinter
import tkinter.messagebox
from tkinter import ttk
import sqlite3
#main page
i=tkinter.Tk(className='blood donation')
i.geometry("1500x1500")
Label(i,text='WELCOME TO BLOOD DONATION PORTAL \n',font=("times new roman","23","bold"),bg='maroon',justify='center').grid(row=0,column=2,columnspan=2)
Label(i,text=' SOME OF YOUR OPTIONS ARE ',font=("arabic","23","bold"),bg='maroon',justify='center').grid(row=1,column=2,columnspan=2)


#already donated
def donatedcallback():
	tkinter.messagebox.showinfo("already donated blood","thank you! you helped save a life ")

#already requested
def requestcallback():
        tkinter.messagebox.showinfo("already requested","thank you! we will try to contact you shortly ")


#donate form
def donateblood():
	top = Tk()
	top.title('blood donation form')
	top.geometry("1500x15000")
	top['bg']='dark red'
	Label(top,text='\t Please fill the below form :',font=("arabic","20","bold"),bg='dark red').grid(row=0)
	Label(top,text='First Name',font=("arabic","17","bold"),bg='dark red').grid(row=3)
	Label(top,text='Last Name',font=("arabic","17","bold"),bg='dark red').grid(row=4)
	Label(top,text='Age',font=("arabic","17","bold"),bg='dark red').grid(row=5)
	Label(top,text='phone number',font=("arabic","17","bold"),bg='dark red').grid(row=6)
	Label(top,text='blood group',font=("arabic","17","bold"),bg='dark red').grid(row=7)
	Label(top,text='email id',font=("arabic","17","bold"),bg='dark red').grid(row=18)
	Label(top,text='gender',font=("arabic","17","bold"),bg='dark red').grid(row=16)
	Label(top,text='remarks',font=("arabic","17","bold"),bg='dark red').grid(row=19)
	e1=Entry(top,font=("arabic",17),width=22)
	e2=Entry(top,font=("arabic",17),width=22)
	e3=Spinbox(top,from_=18,to=50,width=21,font=("arabic","17","bold"),justify='center')
	e4=Entry(top,font=("arabic",17),width=22)
	e6=Entry(top,font=("arabic",17),width=22)
	e7=Entry(top,font=("arabic",17),width=22)
	prev = IntVar()
	chkbx=Checkbutton(top,text='previously donated',font=("arabic","17","bold"),bg='dark red',variable=prev)
	chkbx.grid(row=20,column=1)   
	e1.grid(row=3, column=1)
	e2.grid(row=4, column=1)
	e3.grid(row=5, column=1)
	e4.grid(row=6, column=1)
	goption = StringVar(top,"1")
	valuers = {"Male":"Male","Female":"Female"}
	y=16
	for(text,value) in valuers.items():
		Radiobutton(top,text = text,variable =goption,font=("arabic","17","bold"),selectcolor="green" ,value=value,indicator=0,activebackground="red",background="orange",width=20).grid(row=y,column=1)
		y=y+1
	option = StringVar(top,"1")
	values = {"A+":"A+","A-":"A-","B+":"B+","B-":"B-","O+":"O+","O-":"O-","AB+":"AB+","AB-":"AB-",}
	x=7
	for(text,value) in values.items():
		Radiobutton(top,text = text,variable =option,font=("arabic","17","bold"),selectcolor="green" ,value=value,indicator=0,activebackground="red",background="light blue",width=20).grid(row=x,column=1)
		x=x+1
	e6.grid(row=18,column=1)
	e7.grid(row=19,column=1)
	def submit():
        #create databse
		conn = sqlite3.connect('blooddonaterequiredlist.db')
		#create cursor
		c=conn.cursor()
		#insert into table
		c.execute("INSERT INTO blooddonationlist VALUES(:f_name,:l_name,:age,:phoneno,:bloodgrp,:gender,:emailid,:feedbck,:prev)",
				{
					'f_name':e1.get(),
					'l_name':e2.get(),
					'age':e3.get(),
					'phoneno':e4.get(),
					'bloodgrp':option.get(),
					'gender':goption.get(),
					'emailid':e6.get(),
					'feedbck':e7.get(),
					'prev':prev.get()
				})	
		conn.commit()
		conn.close()
		#clear text boxes
		e1.delete(0,END)
		e2.delete(0,END)
		e3.delete(0,END)
		e4.delete(0,END)
		option.set(None)
		goption.set(None)
		e6.delete(0,END)
		e7.delete(0,END)
		chkbx.deselect()
		tkinter.messagebox.showinfo("successful","thank you! your data has been added to the databse ")
		top.destroy()
	sub=tkinter.Button(top,text="submit",activebackground="blue",width=20,height=1,bg='green',font=("arabic","18","bold"),command=submit).grid(row=23,column=1)
	deletetop=tkinter.Button(top,text="close window",activebackground="blue",width=20,height=1,bg='black',fg="white",font=("arabic","18","bold"),command=top.destroy).grid(row=23,column=0)

#show donated list
def showstats():
    stat=Tk()
    stat.title('show statistics')
    stat.geometry("1500x1500")
    stat['bg']='#49A'
    #Label(stat,text='the blood goups donated till now are :\n',font=("arabic","22","bold"),bg='#49A').grid(row=0)
    #Label(stat,bg='#49A',text="id firstname   lastname    age      phonenumber        blood group     gender                email id                          remarks     first time \n",font=("arabic","17","bold"),justify=LEFT).grid(row=1)
    appLabel = Label(stat, text="SHOW DONATED LIST",fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(stat)
    tree["columns"] = ("zero","one", "two", "three", "four","five","six","seven","eight","nine","ten")
    tree.heading("zero",text="ID")
    tree.heading("one", text="First Name")
    tree.heading("two", text="Last Name")
    tree.heading("three", text="Age")
    tree.heading("four", text="phone no")
    tree.heading("five", text="blood group")
    tree.heading("six", text="gender")
    tree.heading("seven", text="email id")
    tree.heading("eight", text="renarks")
    tree.heading("nine", text="first time")   
    tree.column("zero",width=50,anchor='center')
    tree.column("one",width=100,anchor="center")
    tree.column("two",width=100,anchor="center")
    tree.column("three",width=100,anchor="center")
    tree.column("four",width=150,anchor="center")
    tree.column("five",width=100,anchor="center")
    tree.column("six",width=100,anchor="center")
    tree.column("seven",width=200,anchor="center")
    tree.column("eight",width=100,anchor="center")
    tree.column("nine",width=100,anchor="center")
  #create databse
    conn = sqlite3.connect('blooddonaterequiredlist.db')

    #create cursor
    c=conn.cursor()
    c.execute("SELECT *,oid FROM blooddonationlist ;")
    i = 0

    for row in c :
        tree.insert('',"end",i,text="",values=(row[9],row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
        i = i + 1

    tree.pack()
    conn.commit()
    conn.close()
    stat.mainloop()
    

#delete from donated list
def deleted():
	deler = Tk()
	deler.title('delete an entry ')
	deler.geometry('1500x1500')
	deler['bg']='orangered'
	delet=Label(deler,text="please enter the id of the entry to be deleted in the below box ",font=('arabic',"20","bold italic"))
	delet['bg']='orangered'
	delet.grid(row=5,column=5,padx=10,pady=10)
	deletr=Entry(deler,font=('arabic',"20","bold italic"),width=23)
	deletr.grid(row=15,column=5,padx=10,pady=10)
	def deleterow():
		#create databse
		conn = sqlite3.connect('blooddonaterequiredlist.db')
		#create cursor
		c=conn.cursor()
		#delete a record
		c.execute("DELETE from blooddonationlist WHERE oid = " + deletr.get())
		conn.commit()
		conn.close()
		deletr.delete(0,END)
		tkinter.messagebox.showinfo("successful","your data has been deleted from the databse ")
		deler.destroy()
	rowdel=tkinter.Button(deler, text='delete from list',font=('arabic',"20","bold italic"),width=20,bd=5,height=1,bg='red',activebackground="blue",command=deleterow).grid(row=16,column=5)

#requirement form
def reqbloodform():
	req = Tk()
	req.title('blood requirement form')
	req.geometry("1500x1500")
	req['bg']='dark red'
	Label(req,text='\t Please fill the below form :',font=("arabic","20","bold"),bg='dark red').grid(row=0)
	Label(req,text='First Name',font=("arabic","17","bold"),bg='dark red').grid(row=3)
	Label(req,text='Last Name',font=("arabic","17","bold"),bg='dark red').grid(row=4)
	Label(req,text='Age',font=("arabic","17","bold"),bg='dark red').grid(row=5)
	Label(req,text='phone number',font=("arabic","17","bold"),bg='dark red').grid(row=6)
	Label(req,text='required blood group',font=("arabic","17","bold"),bg='dark red').grid(row=7)
	Label(req,text='email id',font=("arabic","17","bold"),bg='dark red').grid(row=18)
	Label(req,text='gender',font=("arabic","17","bold"),bg='dark red').grid(row=16)
	Label(req,text='ever donated',font=("arabic","17","bold"),bg='dark red').grid(row=19)
	r1=Entry(req,font=("arabic",17),width=22)
	r2=Entry(req,font=("arabic",17),width=22)
	r3=Spinbox(req,from_=18,to=50,width=21,font=("arabic","17","bold"),justify='center')
	r4=Entry(req,font=("arabic",17),width=22)
	r6=Entry(req,font=("arabic",17),width=22)
	r7=Entry(req,font=("arabic",17),width=22)
	reqprev = IntVar()
	#chkbx=Checkbutton(top,text='previously donated',font=("arabic",17),variable=prev)
	#chkbx.grid(row=20,column=1)   
	r1.grid(row=3, column=1)
	r2.grid(row=4, column=1)
	r3.grid(row=5, column=1)
	r4.grid(row=6, column=1)
	reqgoption = StringVar(req,"1")
	valuers = {"Male":"Male","Female":"Female"}
	y=16
	for(text,value) in valuers.items():
		Radiobutton(req,text = text,variable =reqgoption,font=("arabic","17","bold"),selectcolor="green" ,value=value,indicator=0,activebackground="red",background="orange",width=20).grid(row=y,column=1)
		y=y+1
	reqoption = StringVar(req,"1")
	values = {"A+":"A+","A-":"A-","B+":"B+","B-":"B-","O+":"O+","O-":"O-","AB+":"AB+","AB-":"AB-",}
	x=7
	for(text,value) in values.items():
		Radiobutton(req,text = text,variable =reqoption,font=("arabic","17","bold"),selectcolor="green" ,value=value,indicator=0,activebackground="red",background="light blue",width=20).grid(row=x,column=1)
		x=x+1
	r6.grid(row=18,column=1)
	r7.grid(row=19,column=1)
	def reqsubmit():
        #create databse
		conn = sqlite3.connect('blooddonaterequiredlist.db')
		#create cursor
		rc=conn.cursor()
		#insert into table
		rc.execute("INSERT INTO bloodrequiredlist VALUES (:f_name,:l_name,:age,:phoneno,:bloodgrp,:gender,:emailid,:everdonated)",
					{
						'f_name':r1.get(),
						'l_name':r2.get(),
						'age':r3.get(),
						'phoneno':r4.get(),
						'bloodgrp':reqoption.get(),
						'gender':reqgoption.get(),
						'emailid':r6.get(),
						'everdonated':r7.get()
					}
				)
		conn.commit()
		conn.close()
		#clear text boxes
		r1.delete(0,END)
		r2.delete(0,END)
		r3.delete(0,END)
		r4.delete(0,END)
		reqoption.set(None)
		reqgoption.set(None)
		r6.delete(0,END)
		r7.delete(0,END)
		#chkbx.deselect()
		tkinter.messagebox.showinfo("successful","thank you! your data has been added to the required blood list ")
		req.destroy()
	sub=tkinter.Button(req,text="submit",activebackground="blue",width=18,height=1,bg='green',font=("arabic","20","bold"),command=reqsubmit).grid(row=23,column=1)
	deletetop=tkinter.Button(req,text="close window",activebackground="blue",fg="white",width=18,height=1,bg='black',font=("arabic","20","bold"),command=req.destroy).grid(row=23,column=0)

#show requirement list
def showreq():
    reqstat=Tk()
    reqstat.title('show requirement list')
    reqstat.geometry("1500x1500")
    reqstat['bg']='#49A'
	#Label(reqstat,text='the blood goups required til now are :\n',font=("arabic","22","bold"),bg='#49A').grid(row=0)
	#Label(reqstat,bg='#49A',text="  id   firstname   lastname    age   phonenumber  blood group   gender                email id                    ever donated \n",font=("arabic","17","bold"),justify=LEFT).grid(row=1)
	#create databse
    conn = sqlite3.connect('blooddonaterequiredlist.db')

    #create cursor
    c=conn.cursor()
    
    '''c.execute("SELECT *,oid FROM bloodrequiredlist")
	reqrecords=c.fetchall()
    #loop results
	print_reqrecord = ''
	for record in reqrecords:
	    print_reqrecord += str(record[8])+"    "+str(record[0]) +"\t " +str(record[1]) +"\t  "+str(record[2]) +" \t " + str(record[3]) +"  \t  "+str(record[4]) +"\t"+str(record[5]) +" \t "+str(record[6]) +" \t "+str(record[7])+"\n" 
        
	reqquery_label = Label(reqstat,text=print_reqrecord,font=("arabic","18","bold"),bg='#49A',justify='left')
	reqquery_label.grid(row=15,column=0,columnspan=2) 
    
    
	conn.commit()

	conn.close()''' 
    appLabel = Label(reqstat, text="SHOW REQUIRED LIST",fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen", 30))
    appLabel.pack()

    tree = ttk.Treeview(reqstat)
    tree["columns"] = ("zero","one", "two", "three", "four","five","six","seven","eight","nine","ten")
    tree.heading("zero",text="ID")
    tree.heading("one", text="First Name")
    tree.heading("two", text="Last Name")
    tree.heading("three", text="Age")
    tree.heading("four", text="phone no")
    tree.heading("five", text="blood group")
    tree.heading("six", text="gender")
    tree.heading("seven", text="email id")
    tree.heading("eight", text="previously donated")   
    tree.column("zero",width=50,anchor='center')
    tree.column("one",width=100,anchor="center")
    tree.column("two",width=100,anchor="center")
    tree.column("three",width=100,anchor="center")
    tree.column("four",width=150,anchor="center")
    tree.column("five",width=100,anchor="center")
    tree.column("six",width=100,anchor="center")
    tree.column("seven",width=200,anchor="center")
    tree.column("eight",width=150,anchor="center")
  
    
    c.execute("SELECT *,oid FROM bloodrequiredlist ;")
    i = 0

    for row in c :
        tree.insert('',"end",i,text="",values=(row[8],row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
        i = i + 1

    tree.pack()
    conn.commit()
    conn.close()
    reqstat.mainloop()
    
#delete from req list
def deletedreq():
	reqdeler = Tk()
	reqdeler.title('delete an entry ')
	reqdeler.geometry('1500x1500')
	reqdeler['bg']='orangered'
	reqdelet=Label(reqdeler,text="please enter the id of the entry to be deleted from reqirement in the below box ",font=('arabic',"20","bold italic"))
	reqdelet['bg']='orangered'
	reqdelet.grid(row=5,column=5,padx=10,pady=10)
	reqdeletr=Entry(reqdeler,font=('arabic',"20","bold italic"),width=29)
	reqdeletr.grid(row=15,column=5,padx=10,pady=10)
	def deleterow():
		#create databse
		conn = sqlite3.connect('blooddonaterequiredlist.db')
		#create cursor
		c=conn.cursor()
		#delete a record
		c.execute("DELETE from bloodrequiredlist WHERE oid = " + reqdeletr.get())
		conn.commit()
		conn.close()
		reqdeletr.delete(0,END)
		tkinter.messagebox.showinfo("successful","your data has been deleted from the requirement databse ")
		reqdeler.destroy()
	reqrowdel=tkinter.Button(reqdeler, text='delete from list',font=('arabic',"20","bold italic"),width=25,bd=5,height=1,bg='red',activebackground="blue",command=deleterow).grid(row=16,column=5)

#create database
def createdatabase():
	import sqlite3 
	#databse
	conn = sqlite3.connect('blooddonaterequiredlist.db')
	c = conn.cursor()
	#create table
	c.execute("""CREATE TABLE IF NOT EXISTS blooddonationlist (
            firstname text,
            lastname text,
            age integer,
            phone_number integer,
            bloodgroup varchar,
            gender text,
            emailid varchar,
            feedback text,
            prevdon boolean
            )"""
       )

	conn.commit()
	conn.close()
	tkinter.messagebox.showinfo("successful","you created table for blood donation list ")
	conn = sqlite3.connect('blooddonaterequiredlist.db')
	c = conn.cursor()
	#create table
	c.execute("""CREATE TABLE  IF NOT EXISTS bloodrequiredlist (
            firstname text,
            lastname text,
            age integer,
            phone_number integer,
            reqbloodgroup varchar,
            gender text,
            emailid varchar,
            everdonated text
            )""")
	conn.commit()
	conn.close()
	tkinter.messagebox.showinfo("successful","you created table for blood required list ")


#buttons

#donate form
b1=tkinter.Button(i, text='Donate Form',font=("arabic","20","bold"),width=20,bd=5,activebackground="black",activeforeground="white",height=2,bg='light blue',command=donateblood,borderwidth=10).grid(row=7,column=1)
#show donated list
b2=tkinter.Button(i,text='Show Donated List',font=("arabic","20","bold"),width=20,bd=5,activebackground="black",activeforeground="white",height=2,bg='aqua',command=showstats,borderwidth=10).grid(row=15,column=1)
#delete from donated list button
b3=tkinter.Button(i, text='Delete From Donated List',font=("arabic","20","bold"),width=20,bd=5,height=2,bg='blue',activebackground="black",activeforeground="white",command=deleted,justify='center',borderwidth=10).grid(row=30,column=1)
#request submitted
b4=tkinter.Button(i,text="Request Submitted",font=("arabic","20","bold"),width=20,bd=5,height=2,bg="light green",activebackground="black",activeforeground="white",command=requestcallback,borderwidth=10,justify='center').grid(row=7,column=2,columnspan=2)
#already donated
b5=tkinter.Button(i,text="Already Donated",font=("arabic","20","bold"),width=20,bd=5,height=2,bg="green",activebackground="black",activeforeground="white",command=donatedcallback,borderwidth=10,justify='center').grid(row=15,column=2,columnspan=2)
#close button
b6=tkinter.Button(i, text='Close This Window',font=("arabic","20","bold"),width=20,bd=5,height=2,bg='black',fg='white',activebackground="black",activeforeground="white",command=i.destroy,justify='center',borderwidth=10).grid(row=30,column=2,columnspan=2)
#requirement form
b7=tkinter.Button(i, text='Required Blood Form ',font=("arabic","20","bold"),width=17,bd=5,height=2,bg='gold',activebackground="black",activeforeground="white",borderwidth=10,command=reqbloodform).grid(row=7,column=4)
#show req list
b8=tkinter.Button(i, text='Show Required List ',font=("arabic","20","bold"),width=17,bd=5,height=2,bg='dark orange',activebackground="black",activeforeground="white",borderwidth=10,command=showreq).grid(row=15,column=4)
#delete from requirement list
b9=tkinter.Button(i, text='Delete From Req List',font=("arabic","20","bold"),width=17,bd=5,height=2,bg='red',activebackground="black",activeforeground="white",command=deletedreq,justify='center',borderwidth=10).grid(row=30,column=4)
#create database
b10=tkinter.Button(i, text='Click Here To Create Database If You Are Using For The First Time',font=("arabic","20","bold"),width=55,bd=5,height=2,bg='pink',activebackground="black",activeforeground="red",command=createdatabase,justify='center',borderwidth=10).grid(row=35,column=1,columnspan=4)

Label(i,text="\n SPARE ONLY 15 MINUTES AND SAFE A LIFE \nSTARVE A VAMPIRE , DONATE BLOOD" ,font=("arabic","20","italic bold"),bg='maroon',justify='center').grid(row=40,column=1,columnspan=4)
Label(i,text="YOU DON'T NEED SUPERPOWERS TO BE A HERO ,YOU CAN BECOME ONE BY DONATING BLOOD",font=("arabic","20","bold"),bg='maroon',justify='center').grid(row=41,column=1,columnspan=4)
i['bg']='maroon'
i.mainloop()
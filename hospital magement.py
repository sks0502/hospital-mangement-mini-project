from tkinter import *
from tkinter import Text,Tk
import os
import sqlite3
from tkinter import ttk, messagebox
import tkinter as tk

#---------------------------------------------------------------Login Function --------------------------------------
def clear():
	userentry.delete(0,END)
	passentry.delete(0,END)
def close():
        win.destroy()


def login():

        user1=user_name.get()
        pass1=password.get()

        con = sqlite3.connect('reg.db')
        with con:
                cursor=con.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Register (first_name TEXT NOT NULL ,last_name TEXT NOT NULL ,age INTEGER NOT NULL ,gender,city TEXT,address TEXT,user TEXT NOT NULL ,passwd TEXT NOT NULL,very_pass TEXT NOT NULL ,docter TEXT  ,day TEXT ,month TEXT ,year INTEGER,mobile INTEGER )')
        cursor.execute('select * from Register Where user=? AND passwd=?',(user1,pass1))

        if cursor.fetchone() is not None:
                messagebox.showinfo("Success" , "Successfully Login" , parent = win)
                
                deshboard()
                close()
                con.close()
                
        else:
                
                messagebox.showerror("Error" , "Invalid User Name And Password", parent = win)

        
	
	

#---------------------------------------------------- DeshBoard Panel -----------------------------------------
def deshboard():
        def book():
                docter1=Docter.get()
                day1=day.get()
                month1=month.get()
                year1=Year.get()
                user1=user_name.get()
                mobile1=mobile.get()
                con = sqlite3.connect('reg.db')
                cursor = con.cursor()
                cursor.execute("update Register set docter = '" + docter1 + "' ,day = '" +  day1 + "',month='" + month1+ "',year='" + year1 + "',mobile='"+ mobile1 +"' WHERE user ='"+ user1 +"'" )
                con.commit()
                con.close()
                messagebox.showinfo("Success" , "Booked Appointment " , parent = des)     
		


        des = Tk()
        des.title("Appointment Portal")	
        des.maxsize(width=800 ,  height=500)
        des.minsize(width=800 ,  height=500)
        
        label=Label(des,text=f"{user_name.get()}",width=20,height=2,borderwidth=1,relief="sunken",fg="green",bg="white")
        label.grid(column=2,row=3,padx=650,pady=40)

        f=Frame(des,height=1,width=800,bg="black")
        f.place(x=0,y=95)

        con = sqlite3.connect('reg.db')
        cursor = con.cursor()

        cursor.execute("select * from Register where user ='"+ user_name.get() + "'")
        row = cursor.fetchall()

        a=Frame(des,height=1,width=400,bg="black")
        a.place(x=0,y=195)

        b=Frame(des,height=100,width=1,bg="black")
        b.place(x=400,y=97)

        for data in row:
                first_name = Label(des, text= f"Name : {data[0]}" , font='Verdana 10 bold')
                first_name.place(x=20,y=100)
                gender = Label(des, text= f"Gender : {data[3]}" , font='Verdana 10 bold')
                gender.place(x=20,y=130)

                age = Label(des, text= f"Age : {data[2]}" , font='Verdana 10 bold')
                age.place(x=20,y=160)
                mobile = Label(des, text= f"Phone : {data[13]}" , font='Verdana 10 bold')
                mobile.place(x=240,y=100)

                city = Label(des, text= f"City : {data[4]}" , font='Verdana 10 bold')
                city.place(x=240,y=130)

                add = Label(des, text= f"Address : {data[5]}" , font='Verdana 10 bold')
                add.place(x=240,y=160)

	# Book Docter Appointment App
        heading = Label(des , text = "Book Appointment" , font = 'Verdana 20 bold')
        heading.place(x=470 , y=100)	

	# Book DocterLabel 
        Docter= Label(des, text= "Docter:" , font='Verdana 10 bold')
        Docter.place(x=470,y=145)

        Day = Label(des, text= "Day:" , font='Verdana 10 bold')
        Day.place(x=470,y=165)

        Month = Label(des, text= "Month:" , font='Verdana 10 bold')
        Month.place(x=470,y=185)

        Year = Label(des, text= "Year:" , font='Verdana 10 bold')
        Year.place(x=470,y=205)

        mobile = Label(des,text="Mobile:",font='Verdana 10 bold')
        mobile.place(x=470,y=225)


	# Book Docter Entry Box
        docter= StringVar()
        day = StringVar()
        month = StringVar()
        year = StringVar()


	
        mobile = Entry(des, width=33 , textvariable = mobile)
        mobile.place(x=550 , y=230)
        Year = Entry(des, width=33 , textvariable = year)
        Year.place(x=550 , y=210)



        Docter= ttk.Combobox(des, width=30, textvariable= docter, state='readonly')
        Docter['values']=('Andy','Charlie','Shetal','Danish','Sunil')
        Docter.current()
        Docter.place(x=550,y=150)
        day= ttk.Combobox(des, width=30, textvariable= day, state='readonly')
        day['values']=('Monday','Tuesday','Wednesday','Thursday','Friday','Satuday','Sunday')
        day.current()
        day.place(x=550,y=170)
        month= ttk.Combobox(des, width=30, textvariable=month, state='readonly')
        month['values']=('January','February','March','April','May','June','July','August','September','October','November','December')
        month.current()
        month.place(x=550,y=190)

	# button 

        btn= Button(des, text = "Book" ,font='Verdana 10 bold', width = 22, command = book)
        btn.place(x=550, y=250)

       




        con= sqlite3.connect('reg.db')
        cursor= con.cursor()

        cursor.execute("select * from Register where user ='"+ user_name.get() + "'")
        rows = cursor.fetchall()
	# book Appoitment Details
        heading = Label(des , text ="Previous Appointments" , font = 'Verdana 15 bold')
        heading.place(x=20 , y=250)	

        for book in rows:
                d1 = Label(des, text= f"Docter: {book[9]}" , font='Verdana 10 bold')
                d1.place(x=20,y=300)
                d2 = Label(des, text= f"Day: {book[10]}" , font='Verdana 10 bold')
                d2.place(x=20,y=320)
                d3 = Label(des, text= f"Month: {book[11]}" , font='Verdana 10 bold')
                d3.place(x=20,y=340)
                d4 = Label(des, text= f"Year: {book[12]}" , font='Verdana 10 bold')
                d4.place(x=20,y=360)
        	



					


#---------------------register function----------------------- 


def signup():
        def database():
                name1=first_name.get()
                sname1=last_name.get()
                age1=age.get()
                var1=(var.get(),)
                city1=city.get()
                add1=add.get()
                user1=(user_name.get(),)
                pass1=password.get()
                pass2=very_pass.get()
                if first_name.get()=="" or last_name.get()=="" or age.get()=="" or city.get()=="" or add.get()=="" or user_name.get()=="" or password.get()=="" or very_pass.get()=="" :
                        messagebox.showerror("Error" , "All Fields Are Required" , parent = winsignup)
                elif password.get() != very_pass.get():
                        messagebox.showerror("Error" , "Password & Confirm Password Should Be Same" , parent = winsignup)

                else:
                        try:
                                con=sqlite3.connect('reg.db')
                                cursor=con.cursor()
                                cursor.execute("select * from Register where user=?",user1)
                                row = cursor.fetchone()
                                if row!=None:
                                        messagebox.showerror("Error" , "User Name Already Exits", parent = winsignup)
                                else:
                                        cursor.execute('INSERT INTO Register(first_name,last_name,age,gender,city,address,user,passwd,very_pass) VALUES(?,?,?,?,?,?,?,?,?)',(name1,sname1,age1,var1[0],city1,add1,user1[0],pass1,pass2,))
                                        
                                        con.commit()
                                        con.close()
                                        messagebox.showinfo("Success" , "Registration Successfull" , parent = winsignup)
                                        clear()
                                        switch()
                        except Exception as es:
                                messagebox.showerror("Error" , f"Error Dui to : {str(es)}", parent = winsignup)
        
	

        
# close signup function			
        def switch():
                winsignup.destroy()

# clear data function
        def clear():
            first_name.delete(0,END)
            last_name.delete(0,END)
            age.delete(0,END)
            var.delete(0,END)
            city.delete(0,END)
            add.delete(0,END)
            user_name.delete(0,END)
            password.delete(0,END)
            very_pass.delete(0,END)
	
						
                                                                

                                                                             # start Signup Window	
        winsignup = Tk() 
        winsignup.title("sign up ")
        winsignup.maxsize(width=500 ,  height=600)
        winsignup.minsize(width=500 ,  height=600)


#heading label
        heading = Label(winsignup , text = "Signup" , font = 'Verdana 20 bold')
        heading.place(x=80 , y=60)

# form data label
        first_name = Label(winsignup, text= "First Name :" , font='Verdana 10 bold')
        first_name.place(x=80,y=130)

        last_name = Label(winsignup, text= "Last Name :" , font='Verdana 10 bold')
        last_name.place(x=80,y=160)

        age = Label(winsignup, text= "Age :" , font='Verdana 10 bold')
        age.place(x=80,y=190)

        Gender = Label(winsignup, text= "Gender :" , font='Verdana 10 bold')
        Gender.place(x=80,y=220)

        city = Label(winsignup, text= "City :" , font='Verdana 10 bold')
        city.place(x=80,y=260)

        add = Label(winsignup, text= "Address :" , font='Verdana 10 bold')
        add.place(x=80,y=290)

        user_name = Label(winsignup, text= "User Name :" , font='Verdana 10 bold')
        user_name.place(x=80,y=320)

        password = Label(winsignup, text= "Password :" , font='Verdana 10 bold')
        password.place(x=80,y=350)

        very_pass = Label(winsignup, text= "Verify Password:" , font='Verdana 10 bold')
        very_pass.place(x=80,y=380)

# Entry Box ------------------------------------------------------------------
        first_name = StringVar()
        last_name = StringVar()
        age = IntVar(winsignup, value='0')
        var= StringVar()
        city= StringVar()
        add = StringVar()
        user_name = StringVar()
        password = StringVar()
        very_pass = StringVar()
        
        

	
        first_name = Entry(winsignup, width=40 , textvariable = first_name)
        first_name.place(x=200 , y=133)


	
        last_name = Entry(winsignup, width=40 , textvariable = last_name)
        last_name.place(x=200 , y=163)

        age = Entry(winsignup, width=40, textvariable=age)
        age.place(x=200 , y=193)

	
    
        var= ttk.Combobox(winsignup, width=30, textvariable= var, state='readonly')
        var['values']=('Male','Female','Transgender')
        var.current()
        var.place(x=200,y=220)

        city = Entry(winsignup, width=40,textvariable = city)
        city.place(x=200 , y=263)


        add = Entry(winsignup, width=40 , textvariable = add)
        add.place(x=200 , y=293)

	
        user_name = Entry(winsignup, width=40,textvariable = user_name)
        user_name.place(x=200 , y=323)

	
        password = Entry(winsignup, width=40, textvariable = password)
        password.place(x=200 , y=353)

	
        very_pass= Entry(winsignup, width=40 ,show="*" , textvariable = very_pass)
        very_pass.place(x=200 , y=383)


# button login and clear

        btn_signup = Button(winsignup, text = "Signup" ,font='Verdana 10 bold', command = database)
        btn_signup.place(x=200, y=413)


        btn_login = Button(winsignup, text = "Clear" ,font='Verdana 10 bold' , command = clear)
        btn_login.place(x=280, y=413)


        sign_up_btn = Button(winsignup , text="Switch To Login" , command = switch )
        sign_up_btn.place(x=350 , y =20)


        winsignup.mainloop()

#--------------------------------------------------------------

    
win = Tk()

#app title
win.title("Hostpital mangement portal")

#size of main window
win.maxsize(width=500 ,  height=500)
win.minsize(width=500 ,  height=500)

#heading label to main window 
Label(text="HOSPITAL MANGEMENT", bg="light blue", width="300", height="4", font=("Calibri", 16,"bold")).pack()
Label(win , text="").pack()

heading = Label(win , text = "Login" , font = 'Verdana 25 bold')
heading.place(x=80 , y=150)

#.............................


username = Label(win, text= "User Name :" , font='Verdana 10 bold')
username.place(x=80,y=220)

userpass = Label(win, text= "Password :" , font='Verdana 10 bold')
userpass.place(x=80,y=260)

# entry box

user_name = StringVar()
password = StringVar()
	
userentry = Entry(win, width=40 , textvariable = user_name)
userentry.focus()
userentry.place(x=200 , y=223)

passentry = Entry(win, width=40, show="*" ,textvariable = password)
passentry.place(x=200 , y=260)

# button  (login and clear)

btn_login = Button(win, text = "Login" ,font='Verdana 10 bold',command = login)
btn_login.place(x=200, y=293)


btn_login = Button(win, text = "Clear" ,font='Verdana 10 bold', command = clear)
btn_login.place(x=260, y=293)

# signup button

sign_up_btn = Button(win , text="Register" , command = signup )

sign_up_btn.place(x=420 , y =70)





win.mainloop()



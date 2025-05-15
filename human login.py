import tkinter as tk 
from tkinter import ttk, LEFT, END
import sqlite3
from tkinter import messagebox as ms
from PIL import Image,ImageTk
import re

root=tk.Tk()
root.configure(background='white')

w,h=root.winfo_screenwidth(),root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w,h))
root.title("login")

image2=Image.open('h1.jpg')
image2=image2.resize((w,h),Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root,image=background_image)
background_label.image = background_image
background_label.place(x=0,y=0)

#############################################################################################################


Email = tk.StringVar()
password = tk.StringVar() 

def reg():
     from subprocess import call
     call(["python","human registration.py"])
     root.destroy()
     
def log():
    # Establish Connection
    with sqlite3.connect('knee.db') as db:
         c = db.cursor()

        # Find user If there is any take proper action
         db = sqlite3.connect('knee.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS KneeReg"
                        "(name TEXT, address TEXT,  Email TEXT, country TEXT, Phoneno TEXT, Gender TEXT, password TEXT)")
         db.commit()
         
         
         find_entry = ('SELECT * FROM KneeReg WHERE Email = ? and password = ?')
         
         c.execute(find_entry, [(Email.get()), (password.get())])
         result = c.fetchall()
         if result:
            msg = ""
          
            print(msg)
            ms.showinfo("messege", "Login sucessfully")
            

            from subprocess import call
            call(['python',' GUI_Master.py'])
            
           
         
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')


a11=tk. Label(root,text='Login here ',fg='black',bg ='#c0392b',font=('Forte',25)).place(x=200,y=50)

canvas1=tk.Canvas(root,background="black")
canvas1.place(x=50,y=100,width=450,height=350)

#login=Label(root,text="Login",font=('Arial',25),foreground='green').place(x=270,y=350)
a11=tk. Label(root,text='Enter Email',fg='white',bg='black',font=('Cambria',14)).place(x=80,y=145)
a12=tk. Label(root,text='Enter Password',fg='white',bg='black',font=('Cambria',14)).place(x=80,y=195)

b11=tk.Entry(root,width=40, textvariable=Email).place(x=250,y=150,)
b12=tk. Entry(root,width=40,show='*', textvariable=password).place(x=250,y=200,)


def forgot():
    from subprocess import call
    call(['python','forgot password.py'])


button2=tk.Button(root,text="Forgot Password?",fg='black',bg='#5499c7',command=forgot)
button2.place(x=355,y=250)



button2=tk.Button(root,text="Log in",font=("Bold",9),command=log,width=50,bg='#28b463')
button2.place(x=100,y=300)

a=tk. Label(root,text='Not a Member?',font=('Cambria',12),fg='white',bg='black').place(x=290,y=370)


button1=tk.Button(root,text="sign up",fg='black',bg='#5499c7',command=reg)
button1.place(x=405,y=370,width=55)



def window():
  root.destroy()
  
root.mainloop()
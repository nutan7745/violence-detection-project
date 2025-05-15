import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter import messagebox as ms

##############################################+=============================================================
root = tk.Tk()
root.configure(background="skyblue")



w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("human violent detection")


#####For background Image


image2 = Image.open("h6.jpg")
image2 = image2.resize((w,h), Image.LANCZOS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)


label_l1 = tk.Label(root, text="Human Violence Detection",font=("Times New Roman",30, 'bold'),
                    background="#909497",borderwidth=5,relief='solid', fg="#b03a2e",padx=300,pady=40)
label_l1.place(x=250, y=0)


# img1 = Image.open('img4.jpg')
# img1 = img1.resize((150,90), Image.ANTIALIAS)
# logo_image1 = ImageTk.PhotoImage(img1)

# logo_label1 = tk.Label(root, image=logo_image1)
# logo_label1.image = logo_image1
# logo_label1.place(x=15, y=10)


def log():
    from subprocess import call
    call(["python"," human login.py"])
    
def reg():
    from subprocess import call
    call(["python"," human registration.py"])
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Login", command=log, width=12, height=1,font=('times', 20, ' bold '), bg="#5499c7", fg="black")
button1.place(x=100, y=700)

button2 = tk.Button(root, text="Register",command=reg,width=12, height=1,font=('times', 20, ' bold '), bg="#5499c7", fg="black")
button2.place(x=400, y=700)

button3 = tk.Button(root, text="Exit",command=window,width=12, height=1,font=('times', 20, ' bold '), bg="red", fg="black")
button3.place(x=700, y=700)

  
root.mainloop()
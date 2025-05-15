import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import cv2
import numpy as np
from tkinter import messagebox as ms

global fn

fn=""


##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title(" page")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
# image2 = Image.open('s4.jpg')
# image2 = image2.resize((w,h), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

#
label_l2 = tk.Label(root, text="Video Surveillance System suspicious activity",font=("times", 30, 'bold'),
                    background="Brown", fg="white", width=70, height=2)
label_l2.place(x=0, y=0)





frame_alpr = tk.LabelFrame(root, text=" Details ", width=400, height=300, bd=5, font=('times', 14, ' bold '),bg="pink",fg="black")
frame_alpr.grid(row=0, column=0, sticky='nw')
frame_alpr.place(x=450, y=200)

def uploadvedio():  
    import cv2
    import os
    
      
    # Read the video from specified path
    import tkinter as tk    # from tkinter import Tk for Python 3.x
    from tkinter.filedialog import askopenfilename
    
    
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    
    
    cam = cv2.VideoCapture(filename)
    
        
        
    try:
          
        # creating a folder named data
        if not os.path.exists('data'):
            os.makedirs('data')
      
    # if not created then raise error
    except OSError:
        print ('Error: Creating directory of data')
      
    # frame
    currentframe = 0
      
    while(True):
          
        # reading from frame
        ret,frame = cam.read()
      
        if ret:
            # if video is still left continue creating images
            name = './data/frame' + str(currentframe) + '.jpg'
            print ('Creating...' + name)
      
            # writing the extracted images
            cv2.imwrite(name, frame)
      
            # increasing counter so that it will
            # show how many frames are created
            
            currentframe += 1
        else:
            break
      
    # Release all space and windows once done
    cam.release()
    cv2.destroyAllWindows() 
    ms.showinfo("Message", "Successfully uploaded Video")
        




def window():
  root.destroy()
  
  


button4 = tk.Button(frame_alpr, text="Exit", command=window, width=12, height=1,font=('times 15 bold'),bd=0,bg="red", fg="white")
button4.place(x=130, y=150)

#####################################################################################################################
button3 = tk.Button(frame_alpr, text=" Upload Video ", command=uploadvedio,width=15, height=1, font=('times', 15, ' bold '),bg="GREEN",fg="white")
button3.place(x=100, y=50)


#####################################################################################################################



root.mainloop()
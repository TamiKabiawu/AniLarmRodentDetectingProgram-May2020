from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os 
import detection

#this is just laying out the basics window of the GUI
root = Tk()
root.geometry("500x570")
root.title("Animal Watcher")

#This is used to Style the top of the Window
frame = Frame(root, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH,expand=1)
frame.config(background='light blue')
label = Label(frame,text="Animal Watcher", bg='light blue', font=('Times 35 bold'))
label.pack(side=TOP)

#creates a Tkinter iamge that can be used everywhere Tkinter expects an image object
path = "Fall-beautiful-nature.jpg"
img = ImageTk.PhotoImage(Image.open(path))

#This is used to insert the Image
background_label = Label(root, image=img)
background_label.pack(side=TOP)

#This is what lays out the button
B1 = Button(padx=5,pady=5, text = "START WATCHING", font=('helvetica 15 bold'), bg= 'white', fg='black', relief=GROOVE, command=detectionAlg)
B1.place(x=165, y=104)

#this is a function that calls the detection algorithm in the detection.py file
def detectionAlg():
    os.system('python detection.py')

root.mainloop()


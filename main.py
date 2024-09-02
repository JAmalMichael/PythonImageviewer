from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os


def showImage():
    filename = filedialog.askopenfilename(initialdir=os.getcwd(),
                                          title="Select Image File", filetypes=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All File", "*.*")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    label.configure(image=img)
    label.image=img


root = Tk()

frame = Frame(root)
frame.pack(side=BOTTOM, padx=15, pady=15)

label = Label(root)
label.pack()

btn1=Button(frame, text="Select-Image", command=showImage)
btn1.pack(side=tk.LEFT)

btn2=Button(frame, text="Exit", command=lambda:exit())
btn2.pack(side=tk.LEFT, padx=12)

root.title("Image viewer")
root.geometry("400x450")
root.mainloop()
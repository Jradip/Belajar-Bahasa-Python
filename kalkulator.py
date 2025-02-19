from tkinter import *
import tkinter.font as font
import math

root = Tk()
root.title("CALCULATOR")
root.geometry("310x400")
root["bg"] = "00FFFF"


myfont = font.font(size=15)

e = Entry(root,width=25,borderwidth=0)
e["font"] = myfont
e["bg"] =
e.grid(row=0,column=0,columnspan=4,padx=20,pady=20)

button1 = Button(root,text="1",padx=30,pady=30,command=lambda:angka(1))
button2 = Button(root,text="1",padx=30,pady=30,command=lambda:angka(2))
button3 = Button(root,text="1",padx=30,pady=30,command=lambda:angka(3))
button4 = Button(root,text="1",padx=30,pady=30,command=lambda:angka(4))
button5 = Button(root,text="1",padx=30,pady=30,command=lambda:angka(5))
button6 = Button(root,text="1",padx=30,pady=30,command=lambda:angka(6))
button7 = Button(root,text="1",padx=30,pady=30,command=lambda:angka(7))
button8 = Button(root,text="1",padx=30,pady=30,command=lambda:angka(8))
button9 = Button(root,text="1",padx=30,pady=30,command=lambda:angka(9))
button0 = Button(root,text="1",padx=30,pady=30,command=lambda:angka(0))

root.mainloop()
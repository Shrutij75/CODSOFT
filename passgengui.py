import tkinter
from tkinter import *
import random
import string
import pyperclip
from tkinter.font import Font

root=Tk()
root.config(bg="gray")
root.title("PASSWORD GENERATOR")
root.geometry("500x800")

choice=IntVar()

def generate():
    lett=string.ascii_lowercase
    lett2=string.ascii_uppercase
    num=string.digits
    sym=string.punctuation
    all=lett+lett2+num+sym
    
    lng=int(lngthbox.get())
    if choice.get()==1:
        showtxt.insert(0,random.sample(lett+lett2,lng))
    elif choice.get()==2:
        showtxt.insert(0,random.sample(lett+lett2+num,lng))
    elif choice.get()==3:
        showtxt.insert(0,random.sample(all,lng))
     
    # temp=random.sample(all,int(lngthbox.get()))
    # showtxt.insert(0,temp)

def copy():
    cpypass=showtxt.get()
    pyperclip.copy(cpypass)
    

lab=Label(root,text="Password Generator",font=("times new roman","40","bold"),bg="gray",fg="white")
lab.grid(pady=10)

frst_butt=Radiobutton(root,text="WEAK",value=1,variable=choice,font=Font)
frst_butt.grid(pady=5)

scnd_butt=Radiobutton(root,text="MEDIUM",value=2,variable=choice,font=Font)
scnd_butt.grid(pady=5)

thrd_butt=Radiobutton(root,text="HARD",value=3,variable=choice,font=Font)
thrd_butt.grid(pady=5)

lab2=Label(root,text="Password Length",font=("times new roman","30","bold"),bg="gray",fg="white")
lab2.grid(pady=5)

lngthbox=Spinbox(root,from_=3,to_=18,width=5,font=Font)
lngthbox.grid(pady=5)

genrtebutt=Button(root,text="Generate",font=Font,command=generate)
genrtebutt.grid(pady=5)

showtxt=Entry(root,width=40,bd=4,font=Font)
showtxt.grid(pady=5)

copybutt=Button(root,text="Copy Password",font=Font,command=copy)
copybutt.grid(pady=5)
root.mainloop()
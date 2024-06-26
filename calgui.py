import operator
import tkinter
from tkinter import *

#initialise by none
# first_num,second_num,operator=None
root=Tk()
root.title("CALCULATOR")
root.geometry("300x470")
root.resizable(0,0)
root.configure(background='black')

# we have four group of data like first is the digits then operators,then =,
# and then C i.e.clear so we have to write the code for these group of objects

def get_dig(digit):
    current=lab['text']
    new=current+str(digit)
    lab.config(text=new)

def clr():
    lab.config(text='')

def get_oper(op):
    global first_num,operator
    first_num=int(lab['text'])
    operator=op
    lab.config(text='')
 
def get_res(): 
     global first_num,second_num,operator
     second_num=int(lab['text'])
     
     if operator=='+':
         lab.config(text=str(first_num+second_num))
     elif operator=='-':
         lab.config(text=str(first_num-second_num))
     elif operator=='*':
         lab.config(text=str(first_num*second_num))
     else:
         if second_num=='0':
             lab.config(text='error')
         else:
             lab.config(text=str(first_num/second_num,2))
      
lab=Label(root,text='',bg='black',fg='white')
lab.grid(row=0,column=0,columnspan=5,sticky='w',pady=(50,25))
lab.config(font=('verdana',30,'bold'))

butt7=Button(root,text='7',bg='green',fg='white',width=5,height=3,command=lambda:get_dig(7))
butt7.grid(row=1,column=0)
butt7.config(font=('verdana',14,'bold'))

butt8=Button(root,text='8',bg='green',fg='white',width=5,height=3,command=lambda:get_dig(8))
butt8.grid(row=1,column=1)
butt8.config(font=('verdana',14,'bold'))

butt9=Button(root,text='9',bg='green',fg='white',width=5,height=3,command=lambda:get_dig(9))
butt9.grid(row=1,column=2)
butt9.config(font=('verdana',14,'bold'))

buttplus=Button(root,text='+',bg='light Green',fg='white',width=6,height=3,command=lambda:get_oper('+'))
buttplus.grid(row=1,column=3)
buttplus.config(font=('verdana',14,'bold'))

butt4=Button(root,text='4',bg='green',fg='white',width=5,height=3,command=lambda:get_dig(4))
butt4.grid(row=2,column=0)
butt4.config(font=('verdana',14,'bold'))

butt5=Button(root,text='5',bg='green',fg='white',width=5,height=3,command=lambda:get_dig(5))
butt5.grid(row=2,column=1)
butt5.config(font=('verdana',14,'bold'))

butt6=Button(root,text='6',bg='green',fg='white',width=5,height=3,command=lambda:get_dig(6))
butt6.grid(row=2,column=2)
butt6.config(font=('verdana',14,'bold'))

buttsub=Button(root,text='-',bg='light Green',fg='white',width=6,height=3,command=lambda:get_oper('-'))
buttsub.grid(row=2,column=3)
buttsub.config(font=('verdana',14,'bold'))

butt1=Button(root,text='1',bg='green',fg='white',width=5,height=3,command=lambda:get_dig(1))
butt1.grid(row=3,column=0)
butt1.config(font=('verdana',14,'bold'))

butt2=Button(root,text='2',bg='green',fg='white',width=5,height=3,command=lambda:get_dig(2))
butt2.grid(row=3,column=1)
butt2.config(font=('verdana',14,'bold'))

butt3=Button(root,text='3',bg='green',fg='white',width=5,height=3,command=lambda:get_dig(3))
butt3.grid(row=3,column=2)
butt3.config(font=('verdana',14,'bold'))

buttmulti=Button(root,text='*',bg='light Green',fg='white',width=6,height=3,command=lambda:get_oper('*'))
buttmulti.grid(row=3,column=3)
buttmulti.config(font=('verdana',14,'bold'))

buttdiv=Button(root,text='/',bg='light Green',fg='white',width=6,height=3,command=lambda:get_oper('/'))
buttdiv.grid(row=4,column=3)
buttdiv.config(font=('verdana',14,'bold'))

buttres=Button(root,text='=',bg='light Green',fg='white',width=5,height=3,command=lambda:get_res())
buttres.grid(row=4,column=2)
buttres.config(font=('verdana',14,'bold'))

buttC=Button(root,text='C',bg='light Green',fg='white',width=5,height=3,command=lambda:clr())
buttC.grid(row=4,column=1)
buttC.config(font=('verdana',14,'bold'))

butt0=Button(root,text='0',bg='light Green',fg='white',width=5,height=3,command=lambda:get_dig(0))
butt0.grid(row=4,column=0)
butt0.config(font=('verdana',14,'bold'))



root.mainloop()
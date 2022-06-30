from tkinter import *

window=Tk()
window.geometry('800x500')
window.configure(bg="gainsboro")
calculation=""
x=StringVar()
def onpress(n):
    global calculation
    calculation+=str(n)
    x.set(calculation)
def total():
    global calculation
    totall=str(eval(calculation))
    x.set(totall)
    calculation=''
def clear():
    global calculation
    calculation=''
    x.set(calculation)
def close():
    window.destroy()
entry=Entry(window,textvariable=x,width='50').grid(columnspan='10',padx='10',pady='10')
clear=Button(window,text='CLEAR',bg='red',fg="white",command=clear).grid(row='0',column='6')
number1=Button(window,text='1',height='10',width='10',command=lambda:onpress(1),bg='navy',fg='white').grid(row='1',column='0')
number2=Button(window,text='2',height='10',width='10',command=lambda:onpress(2),bg='navy',fg='white').grid(row='1',column='1')
number3=Button(window,text='3',height='10',width='10',command=lambda:onpress(3),bg='navy',fg='white').grid(row='1',column='2')
number4=Button(window,text='4',height='10',width='10',command=lambda:onpress(4),bg='navy',fg='white').grid(row='2',column='0')
number5=Button(window,text='5',height='10',width='10',command=lambda:onpress(5),bg='navy',fg='white').grid(row='2',column='1')
number6=Button(window,text='6',height='10',width='10',command=lambda:onpress(6),bg='navy',fg='white').grid(row='2',column='2')
number7=Button(window,text='7',height='10',width='10',command=lambda:onpress(7),bg='navy',fg='white').grid(row='3',column='0')
number8=Button(window,text='8',height='10',width='10',command=lambda:onpress(8),bg='navy',fg='white').grid(row='3',column='1')
number9=Button(window,text='9',height='10',width='10',command=lambda:onpress(9),bg='navy',fg='white').grid(row='3',column='2')
numberadd=Button(window,text='+',height='10',width='10',command=lambda:onpress('+'),bg='cornflower blue',fg='white').grid(row='1',column='4')
numbersub=Button(window,text='-',height='10',width='10',command=lambda:onpress('-'),bg='cornflower blue',fg='white').grid(row='2',column='4')
numbermul=Button(window,text='*',height='10',width='10',command=lambda:onpress('*'),bg='cornflower blue',fg='white').grid(row='1',column='5')
numberdiv=Button(window,text='/',height='10',width='10',command=lambda:onpress('/'),bg='cornflower blue',fg='white').grid(row='2',column='5')
number0=Button(window,text='0',height='10',width='10',command=lambda:onpress(1),bg='navy',fg='white').grid(row='3',column='4')
numberequal=Button(window,text='=',height='10',width='10',command=total,bg='dodger blue',fg='white').grid(row='3',column='5')
numbermod=Button(window,text='%',height='10',width='10',command=lambda:onpress('%'),bg='cornflower blue',fg='white').grid(row='1',column='6')
numberpoint=Button(window,text='.',height='10',width='10',command=lambda:onpress('.'),bg='cornflower blue',fg='white').grid(row='2',column='6')
close=Button(window,text="Close",height='10',width='10',command=close,bg="red",fg="white").grid(row='3',column='6')

window.mainloop()

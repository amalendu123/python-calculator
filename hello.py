from tkinter import *

window=Tk()
window.geometry('800x500')
calculation=""
x=StringVar()
def onpress(n):
    global calculation
    calculation+=str(n)
    x.set(calculation)
entry=Entry(window,textvariable=x).grid(columnspan='4',ipadx='70')
number1=Button(window,text='1',height='10',width='10',command=lambda:onpress(1)).grid(row='1',column='0')
number2=Button(window,text='2',height='10',width='10',command=lambda:onpress(2)).grid(row='1',column='1')
number3=Button(window,text='3',height='10',width='10',command=lambda:onpress(3)).grid(row='1',column='2')
number4=Button(window,text='4',height='10',width='10',command=lambda:onpress(4)).grid(row='2',column='0')
number5=Button(window,text='5',height='10',width='10',command=lambda:onpress(5)).grid(row='2',column='1')
number6=Button(window,text='6',height='10',width='10',command=lambda:onpress(6)).grid(row='2',column='2')
number7=Button(window,text='7',height='10',width='10',command=lambda:onpress(7)).grid(row='3',column='0')
number8=Button(window,text='8',height='10',width='10',command=lambda:onpress(8)).grid(row='3',column='1')
number9=Button(window,text='9',height='10',width='10',command=lambda:onpress(9)).grid(row='3',column='2')
numberadd=Button(window,text='+',height='10',width='10').grid(row='1',column='4')
numberequal=Button(window,text='=',height='4',width='4').grid(row='3',column='4')

    

window.mainloop()

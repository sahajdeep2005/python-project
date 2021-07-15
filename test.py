
import math
from tkinter import *
from tkinter import messagebox

screen =Tk()
screen.title('myclaculator')
screen.maxsize(width=450,height=450)
screen.minsize(width=365,height=450)
screen.configure(bg='blue')
p1 = PhotoImage(file = 'Hopstarter-Soft-Scraps-Calculator.png')
screen.iconphoto(False, p1)
def click(number):
        global operator
        operator+=str(number)
        tex.set(operator)
def clean():
    global operator
    operator=''
    tex.set(operator)
def equal():
    global operator
    try:
        result=eval(operator)
        operator=str(result)
        tex.set(operator)
    except:
           messagebox.showinfo('notifaction','Try again something is wrong')

def cmsin():
    global operator
    try:
        result=math.sin(eval(operator))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notifaction','Try again something is wrong')

def cmcos():
    global operator
    try:
        result=math.cos(eval(operator))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notifaction','Try again something is wrong')

def cmtan():
    global operator
    try:
        result=math.tan(eval(operator))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notifaction','Try again something is wrong')

def cmsqrt():
    global operator
    try:
        result=math.sqrt(eval(operator))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notifaction','Try again something is wrong')

def cmlog():
    global operator
    try:
        result=math.log(eval(operator))
        operator=str(result)
        tex.set(operator)
    except:
        messagebox.showinfo('notifaction','Try again something is wrong')


##############################binding funcation
def on_leave7(s):
   btn7.configure(bg='powder blue')
def on_enter7(s):
    btn7.configure(bg='orange')

def on_leave8(s):
    btn8.configure(bg='powder blue')
def on_enter8(s):
    btn8.configure(bg='orange')

def on_leave9(s):
    btn9.configure(bg='powder blue')
def on_enter9(s):
    btn9.configure(bg='orange')

def on_leaveadd(s):
    btnadd.configure(bg='powder blue')
def on_enteradd(s):
    btnadd.configure(bg='orange')

def on_leave4(s):
    btn4.configure(bg='powder blue')
def on_enter4(s):
    btn4.configure(bg='orange')

def on_leave5(s):
    btn5.configure(bg='powder blue')
def on_enter5(s):
    btn5.configure(bg='orange')

def on_leave6(s):
    btn6.configure(bg='powder blue')
def on_enter6(s):
    btn6.configure(bg='orange')

def on_leavesub(s):
    btnsub.configure(bg='powder blue')
def on_entersub(s):
    btnsub.configure(bg='orange')

def on_leave1(s):
    btn1.configure(bg='powder blue')
def on_enter1(s):
    btn1.configure(bg='orange')

def on_leave2(s):
    btn2.configure(bg='powder blue')
def on_enter2(s):
    btn2.configure(bg='orange')

def on_leave3(s):
    btn3.configure(bg='powder blue')
def on_enter3(s):
    btn3.configure(bg='orange')

def on_leavemulti(s):
    btnmulti.configure(bg='powder blue')
def on_entermulti(s):
    btnmulti.configure(bg='orange')

def on_leave0(s):
    btn0.configure(bg='powder blue')
def on_enter0(s):
    btn0.configure(bg='orange')

def on_leaveequal(s):
    btnequal.configure(bg='powder blue')
def on_enterequal(s):
    btnequal.configure(bg='orange')

def on_leaveclean(s):
    btnclean.configure(bg='powder blue')
def on_enterclean(s):
    btnclean.configure(bg='orange')

def on_leavedivi(s):
    btndivi.configure(bg='powder blue')
def on_enterdivi(s):
    btndivi.configure(bg='orange')

def on_enterentry1(s):
    entry1.configure(bg='orange')
def on_leaveentry1(s):
    entry1.configure(bg='powder blue')

def on_leavesin(s):
    btndivi.configure(bg='powder blue')
def on_entersin(s):
    btndivi.configure(bg='orange')

def on_leavecos(s):
    btndivi.configure(bg='powder blue')
def on_entercos(s):
    btndivi.configure(bg='orange')

def on_leavetan(s):
    btndivi.configure(bg='powder blue')
def on_entertan(s):
    btndivi.configure(bg='orange')

def on_leavesqrt(s):
    btndivi.configure(bg='powder blue')
def on_entersqrt(s):
    btndivi.configure(bg='orange')

def on_leavelog(s):
    btndivi.configure(bg='powder blue')
def on_enterlog(s):
    btndivi.configure(bg='orange')
def audio(number):
    btn7.audio(7)


tex=StringVar()
operator=''

entry1=Entry(screen,bg='powder blue',font=('arial' ,20),bd=30,justify='right',textvariable=tex)
entry1.grid(row=0,columnspan=4)


btn7=Button(screen,text='7',font=('arial',15),bd=10,padx=16,pady=16,command=lambda:click(7),activebackground='green',bg='powder blue',)
btn7.grid(row=1,column=0)
btn8=Button(screen,text='8',font=('arial',15),bd=10,padx=16,pady=16,command=lambda:click(8),activebackground='green',bg='powder blue')
btn8.grid(row=1,column=1)


btn9=Button(screen,text='9',font=('arial',15),bd=10,padx=16,pady=16,command=lambda:click(9),activebackground='green',bg='powder blue')
btn9.grid(row=1,column=2)
btnadd=Button(screen,text='+',font=('arial',15),bd=10,padx=16,pady=16,command=lambda:click('+'),activebackground='blue',bg='powder blue')
btnadd.grid(row=1,column=3)

btn4=Button(screen,text='4',font=('arial',15),bd=10,padx=16,pady=16,command=lambda:click(4),activebackground='green',bg='powder blue')
btn4.grid(row=2,column=0)
btn5=Button(screen,text='5',font=('arial',15),bd=10,padx=16,pady=16,command=lambda:click(5),activebackground='green',bg='powder blue')
btn5.grid(row=2,column=1)
btn6=Button(screen,text='6',font=('arial',15),bd=10,padx=16,pady=16,command=lambda:click(6),activebackground='green',bg='powder blue')
btn6.grid(row=2,column=2)
btnsub=Button(screen,text='-',font=('arial',15),bd=10,padx=16,pady=16,command=lambda:click('-'),activebackground='blue',bg='powder blue')
btnsub.grid(row=2,column=3)

btn1=Button(screen,text='1',font=('arial',15),bd=10,padx=16,pady=16,command=lambda:click(1),activebackground='green',bg='powder blue')
btn1.grid(row=3,column=0)
btn2=Button(screen,text='2',font=('arial',15),bd=10,padx=16,pady=16,command=lambda:click(2),activebackground='green',bg='powder blue')
btn2.grid(row=3,column=1)
btn3=Button(screen,text='3',font=('arial',15),bd=10,padx=16,pady=16,command=lambda:click(3),activebackground='green',bg='powder blue')
btn3.grid(row=3,column=2)
btnmulti=Button(screen,text='X',font=('arial',15),bd=10,padx=16,pady=16,command=lambda:click('*'),activebackground='blue',bg='powder blue')
btnmulti.grid(row=3,column=3)

btn0=Button(screen,text='0',font=('arial',15),bd=10,padx=16,pady=16,command=lambda:click(0),activebackground='green',bg='powder blue')
btn0.grid(row=4,column=0)
btnequal=Button(screen,text='=',font=('arial',15),bd=10,padx=16,pady=16,command=equal,activebackground='blue',bg='powder blue')
btnequal.grid(row=4,column=1)
btnclean=Button(screen,text='c',font=('arial',15),bd=10,padx=16,pady=16,command=clean,activebackground='blue',bg='powder blue')
btnclean.grid(row=4,column=2)
btndivi=Button(screen,text='/',font=('arial',15),bd=10,padx=16,pady=16,command=lambda:click('/'),activebackground='blue',bg='powder blue')
btndivi.grid(row=4,column=3)

btnsin=Button(screen,text='sin',font=('arial',15),bd=10,padx=15,pady=15,command=cmsin,activebackground='green',bg='powder blue')
btnsin.grid(row=0,column=4)

btncos=Button(screen,text='cos',font=('arial',15),bd=10,padx=12,pady=15,command=cmcos,activebackground='green',bg='powder blue')
btncos.grid(row=1,column=4)

btntan=Button(screen,text='tan',font=('arial',15),bd=10,padx=14,pady=14,command=cmtan,activebackground='green',bg='powder blue')
btntan.grid(row=2,column=4)

btnsqrt=Button(screen,text='sqrt',font=('arial',15),bd=10,padx=10,pady=15,command=cmsqrt,activebackground='green',bg='powder blue')
btnsqrt.grid(row=3,column=4)

btnlog=Button(screen,text='log',font=('arial',15),bd=10,padx=15,pady=15,command=cmlog,activebackground='green',bg='powder blue')
btnlog.grid(row=4,column=4)








###########################
btnsin.bind('<Enter>',on_entersin)
btnsin.bind('<Leave>',on_leavesin)

btncos.bind('<Enter>',on_entercos)
btncos.bind('<Leave>',on_leavecos)

btntan.bind('<Enter>',on_entertan)
btntan.bind('<Leave>',on_leavetan)

btnsqrt.bind('<Enter>',on_entersqrt)
btnsqrt.bind('<Leave>',on_leavesqrt)

btnlog.bind('<Enter>',on_enterlog)
btnlog.bind('<Leave>',on_leavelog)











entry1.bind('<Enter>',on_enterentry1)
entry1.bind('<Leave>',on_leaveentry1)


btn=btn7.bind('<Enter>',on_enter7 )
btn7.bind('<Leave>',on_leave7)

btn8.bind('<Enter>',on_enter8)
btn8.bind('<Leave>',on_leave8)

btn9.bind('<Enter>',on_enter9)
btn9.bind('<Leave>',on_leave9)

btn6.bind('<Enter>',on_enter6)
btn6.bind('<Leave>',on_leave6)

btn5.bind('<Enter>',on_enter5)
btn5.bind('<Leave>',on_leave5)

btn4.bind('<Enter>',on_enter4)
btn4.bind('<Leave>',on_leave4)

btn3.bind('<Enter>',on_enter3)
btn3.bind('<Leave>',on_leave3)

btn2.bind('<Enter>',on_enter2)
btn2.bind('<Leave>',on_leave2)

btn1.bind('<Enter>',on_enter1)
btn1.bind('<Leave>',on_leave1)

btnmulti.bind('<Enter>',on_entermulti)
btnmulti.bind('<Leave>',on_leavemulti)

btn0.bind('<Enter>',on_enter0)
btn0.bind('<Leave>',on_leave0)

btnadd.bind('<Enter>',on_enteradd)
btnadd.bind('<Leave>',on_leaveadd)

btnsub.bind('<Enter>',on_entersub)
btnsub.bind('<Leave>',on_leavesub)

btnclean.bind('<Enter>',on_enterclean)
btnclean.bind('<Leave>',on_leaveclean)

btnequal.bind('<Enter>',on_enterequal)
btnequal.bind('<Leave>',on_leaveequal)

btndivi.bind('<Enter>',on_enterdivi)
btndivi.bind('<Leave>',on_leavedivi)














screen.mainloop()

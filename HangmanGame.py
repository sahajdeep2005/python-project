from tkinter import*

screen =Tk()
import random
screen.title('Hangman Game')
screen.maxsize(width=600,height=400)
screen.minsize(width=600,height=400)
screen.configure(bg='RosyBrown')
from tkinter import messagebox 
#########################################################

wordlist=['banana','mango','orange','bingo','tingo',
'patato','pen','set','met','get','let','lot','meet','seat',
'jeep','kite','ride','lite','table','banten','github','papaya','github','apples']

wordlist1=['pen','set','met','get','let','lot']
wordlist2=['meet','seat','jeep','kite','ride','lite']
wordlist3=['mango','bingo','tingo','table','banten','github']
wordlist4=['banana','orange','patato','papaya','github','apples']

#########################################################
def chooseword():
    global l1,ss,ss1,n,temps
    ss=random.choice(wordlist)
    l1=["*"for i in ss]
    ss1=len(ss)
    n=ss1
    if n==3:
        wordLabel2.configure(text=wordlist1)
    elif n==4:
        wordLabel2.configure(text=wordlist2)    
    elif n==5:
        wordLabel2.configure(text=wordlist3)
    elif n==6:
        wordLabel2.configure(text=wordlist4)    

    temps=ss
    leftchance.configure(text='Left={}'.format(n-2))
    ffdata=''
    for i in l1:
        ffdata+=i+''
        wordLabel.configure(text=ffdata)
        ans.configure(text='')
def hangman():
    global l1,ss,ss1,n,temps
    first=varname.get()
    entrybox.delete(0,END)
    if n>0:
        if first in ss:
            for i in range(ss1):
                if ss[i]==first and l1[i]=='*':
                    l1.pop(i)
                    l1.insert(i,ss[i])
                    xx=''.join (l1)
                    ss=list(ss)
                    ss.pop(i)
                    ss.insert(i,'*')
                    wordLabel.configure(text=xx)
                    if xx==temps:
                        ans.configure(text='congratulation you win the game')
                        res=messagebox.askyesno('notifaction','you want to play again ')
                        if res==True:
                            chooseword()
                        else:
                            screen.destroy()  
                    else:
                        break
        else:
             n-=1
             leftchance.configure(text='Left={}'.format(n))    

    if n<=0:
                    ans.configure(text='oops you loose the game')
                    res=messagebox.askyesno('notifaction','you want to play again ')
                    if res==True:
                         chooseword()
                    else:
                         screen.destroy()                



def jj(s):
    hangman()



#####################################################333



varname=StringVar()

##############################################################
label=Label(screen,text='Welcome To Hangman Game',bg='RosyBrown',font=('arial',15,'italic bold'))
label.place(x=40,y=10)
wordLabel=Label(screen,text='',font=('arial',40,'italic bold'),bg='RosyBrown',width=5)
wordLabel.place(x=220,y=200)

wordLabel2=Label(screen,text= '',font=('arial',20,'italic bold'),bg='powder blue',width=35)
wordLabel2.place(x=20,y=100)


leftchance=Label(screen,text='',font=('arial',15,'italic bold'),bg='RosyBrown',)
leftchance.place(x=450,y=40)
ans=Label(screen,text='',font=('arial',15,'italic bold'),bg='RosyBrown',)
ans.place(x=10,y=350)

###############################################
entrybox=Entry(screen,textvariable=varname,bd=5,font=('arial',15,'italic bold',),justify ='center' ,width=10)
entrybox.focus_set()
entrybox.place(x=230,y=250)

Btn1=Button(screen,font=('arial',10,'italic bold',),text='submit',bd=5,width=10,bg='powder blue',fg='red',command=hangman)
Btn1.place(x=250,y=300,)


















screen.bind('<Return>',jj)



























chooseword()
screen.mainloop()
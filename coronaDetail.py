from tkinter import*
from bs4 import BeautifulSoup
import requests
import plyer
import pandas as pd
from tkinter import messagebox,filedialog
screen=Tk()
screen.title('Corona App')
screen.maxsize(width=300,height=300)
screen.minsize(width=300,height=300)
screen.configure(bg='wheat1')
def scrap():
    def notifyme(title,message):
        plyer.notification.notify(
        title=title,
        message=message,
        timeout=20 )
    url1='https://www.worldometers.info/coronavirus/'
    e=requests.get(url1)
    soup=BeautifulSoup(e.content,'html.parser')
    tablebody=soup.find('tbody')
    ttt=tablebody.find_all('tr')
    notifycountry=countrydata.get()
    if notifycountry =='':
        notifycountry='india'

    ########################################
    countries,total_cases ,new_cases,total_death,new_death,total_recovred,acative_cases=[],[],[],[],[],[],[]
    serious,totalcases_peraillion,totaldeath_perallion,totaltests,totaltests_perallion=[],[],[],[],[]
    Headers=['countries','total_cases' ,'new_cases','total_death','new_death','total_recovred','acative_cases',
    'serious','totalcases_peraillion','totaldeath_perallion','totaltests','totaltests_perallion']
    for i in ttt:
        id= i.find_all('td')
        if  id[1].text.strip().lower()==notifycountry:
            totalcases=int(id[2].text.strip().replace(',',''))
            newcases=id[3].text.strip()
            totaldeath=id[4].text.strip()
            newdeath=id[5].text.strip()
            notifyme('corona virus detail{}'.format(notifycountry),
                     'total cases:{}\n new cases:{}\n total death:{}\n new death:{}'.format(totalcases,
                                                                                            newcases,
                                                                                            totaldeath,
                                                                                            newdeath))







        countries.append(id[1].text.strip()),
        total_cases.append(id[2].text.strip().replace(',','')),
        new_cases.append(id[3].text.strip()),
        total_death.append(id[4].text.strip()),
        new_death.append(id[5].text.strip()),
        total_recovred.append(id[6].text.strip()),
        acative_cases.append(id[7].text.strip()),
        serious.append(id[8].text.strip()),
        totalcases_peraillion.append(id[9].text.strip()),
        totaldeath_perallion.append(id[10].text.strip()),
        totaltests.append(id[11].text.strip()),
        totaltests_perallion.append(id[12].text.strip())
        df = pd.DataFrame(list(zip(countries,total_cases ,new_cases,total_death,new_death,total_recovred,acative_cases,
        serious,totalcases_peraillion,totaldeath_perallion,totaltests,totaltests_perallion)),columns=Headers)
    sor = df.sort_values('total_cases',ascending=False)
    for k in formatlist:
        if(k == 'html'):
            path2 = '{}/alldata.html'.format(path)
            sor.to_html(r'{}'.format(path2))
        if(k == 'json'):
            path2 = '{}/alldata.json'.format(path)
            sor.to_json(r'{}'.format(path2))
        if(k == 'csv'):
            path2 = '{}/alldata.csv'.format(path)
            sor.to_csv(r'{}'.format(path2))
    if(len(formatlist) !=0):
        messagebox.showinfo("Notification",'Corona Record Is saved {}'.format(path2),parent=root)


def download():
    global path
    if(len(formatlist) != 0):
        path = filedialog.askdirectory()
    else:
        pass
    scrap()
    formatlist.clear()
    btn1.configure(state='normal')
    btn2.configure(state='normal')
    btn3.configure(state='normal')

def inhtml():
    formatlist.append('html')
    btn1.configure(state='disabled')
def incsv():
    formatlist.append('csv')
    btn3.configure(state='disabled')
def injson():
    formatlist.append('json')
    btn2.configure(state='disabled')

##############################################
countrydata=StringVar()
formatlist = []
path = ''

#############################################

label1=Label(screen,text='Corona Virus  info',bg='cornsilk4',font=('arial' ,17,'italic bold'),width=25)
label1.place(x=1,y=1)

label2=Label(screen,text='Country:',bg='cornsilk4',font=('arial' ,13,'italic bold'),width=10)
label2.place(x=7,y=80)

label3=Label(screen,text='Dowloard:',bg='cornsilk4',font=('arial' ,13,'italic bold'),width=10)
label3.place(x=7,y=130)  

entrybox=Entry(screen,textvariable=countrydata,bg='gainsboro',font=('arial' ,13),width=20)
entrybox.place(x=120,y=80)
#######################################################button
btn1=Button(screen,bg='lightsky blue',font=('arial' ,7,'italic bold'),width=5,text='html',bd=7,activebackground='gold',command=inhtml)
btn1.place(x=120,y=130)

btn2=Button(screen,bg='lightsky blue',font=('arial' ,7,'italic bold'),width=5,text='json',bd=7,activebackground='gold',command=injson)
btn2.place(x=180,y=130)

btn3=Button(screen,bg='lightsky blue',font=('arial' ,7,'italic bold'),width=5,text='csv',bd=7,activebackground='gold',command=incsv)
btn3.place(x=240,y=130)

btn4=Button(screen,bg='deep sky blue',font=('arial' ,10,'italic bold'),width=10,text='Submit',bd=7,activebackground='gold',command=download)
btn4.place(x=100,y=250)

screen.mainloop()
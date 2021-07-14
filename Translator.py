from tkinter import*
from textblob import TextBlob
from tkinter.ttk import Combobox
from tkinter import messagebox
screen=Tk()
screen.title('Translator')
screen.maxsize(width=300,height=300)
screen.minsize(width=300,height=300)
screen.configure(bg='ivory2')
varname=StringVar()
varname2=StringVar()
####################################################################################
def click(event=None):
    try:
        word3=TextBlob(varname.get())
        lan=word3.detect_language()
        lan_todict=language.get()
        lan_to=lan_dict[lan_todict]
        word3=word3.translate(from_lang=lan,to=lan_to)
        meanLabel2.configure(text=word3)
        varname2.set(word3)
    except:
        varname2.set('Try another keyword')

def Exit():
   rr= messagebox.askyesno('notification','Are you sure to exit')
   if rr==True:
       screen.destroy()
def on_enterentry1(s):
    entry1['bg']='green yellow'
def on_leaverentry1(s):
    entry1['bg']='cadetBlue1'

def on_enterentry2(s):
    entry2['bg']='green yellow'
def on_leaveentry2(s):
    entry2['bg']='cadetBlue1'


def on_enterbtn1(s):
    btnclick['bg']='green yellow'
def on_leavebtn1(s):
    btnclick['bg']='cadetBlue1'

def on_enterentrybtn2(s):
    btnexit['bg']='green yellow'
def on_leaverentrybtn2(s):
    btnexit['bg']='cadetBlue1'








lan_dict={'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

#########################################################################################  combo box
language=StringVar()
font_combobox=Combobox(screen,textvariable=language,width=10,state='readonly',)
font_combobox['values']=[e for e in lan_dict.keys()]
font_combobox.current(37)
font_combobox.place(x=200,y=0)









##################################################  Enter box

entry1=Entry(screen,bg='cadetBlue1',font=('arial',10,'italic bold'),bd=5,text=varname)
entry1.place(x=120,y=60)

entry2=Entry(screen,bg='cadetBlue1',font=('arial' ,10,'italic bold'),bd=5,textvariable=varname2)
entry2.place(x=120,y=120)
#########################
#
#
# label box
wordLabel=Label(screen,text='Search:',font=('arial',10,'italic bold'),bg='ivory2',width=7)
wordLabel.place(x=10,y=60)
meanLabel1=Label(screen,text='Trnaslator:',font=('arial',10,'italic bold'),bg='ivory2',width=7)
meanLabel1.place(x=10,y=120)
meanLabel2=Label(screen,text='',font=('arial',10,'italic bold'),bg='ivory2',width=7)
meanLabel2.place(x=10,y=250)
##############################################################################   button



btnclick=Button(screen,text='Click',font=('arial',10,'bold'),bd=10,command=click,activebackground='green',bg='cadetBlue1')
btnclick.place(x=30,y=190)

btnexit=Button(screen,text='Exit',font=('arial',10,'bold'),bd=10,command=Exit,activebackground='green',bg='cadetBlue1')
btnexit.place(x=200,y=190)
entry1.bind('<Enter>',on_enterentry1)
entry1.bind('<Leave>',on_leaverentry1)


entry2.bind('<Enter>',on_enterentry2)
entry2.bind('<Leave>',on_leaveentry2)


btnclick.bind('<Enter>',on_enterbtn1)
btnclick.bind('<Leave>',on_leavebtn1)


btnexit.bind('<Enter>',on_enterentrybtn2)
btnexit.bind('<Leave>',on_leaverentrybtn2)

screen.bind('<Return>',click)














screen.mainloop()
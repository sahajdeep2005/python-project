from tkinter import*
from tkinter  import filedialog
from pygame import mixer
from tkinter.ttk import Progressbar
import datetime
from mutagen.mp3 import MP3

screen=Tk()
screen.title(' Apnna Music Player')

screen.maxsize(width=500,height=500)
screen.minsize(width=500,height=500)
screen.configure(bg='lightsky blue')
##############################################

totalmusictime=0
count=0
sliderwords=''
def labelslider():
    global count,sliderwords
    text ='Welcome To Apnna Music>>> '
    if (count>=len(text)):
        count=0
        sliderwords=''
    sliderwords+=text[count]
    count+=1
    fontLabel.configure(text=sliderwords)
    fontLabel.after(150,labelslider)
fontLabel=Label(screen,text='',font=('arial',15,'italic bold'),bg='lightsky blue',width=30)
fontLabel.place(x=80,y=450)
labelslider()
#############################
audiotrack=StringVar()






################################


def musicurl():
    try:
      s=filedialog.askopenfilename(initialdir='C:/Users/palwsing/Downloads',
                                 title= 'Select audio file',
                                  filetype=('MP3','mp3',('wav','WAV')))
    except:
        s=filedialog.askopenfilename(  title= 'Select audio file',
                                     filetype=(('MP3','mp3'),('wav','WAV')))
    audiotrack.set(s)
def play():
    p= audiotrack.get()
    mixer.music.load(p)
    mixer.music.set_volume(0.4)
    progressbarVolume['value']=40
    progressbarVolumelabel['text']='40%'
    mixer.music.play()

    audiolabel.configure(text='Playing..')
    song=MP3(p)
    totalmusictime=int(song.info.length)
    progressbarmusic['maximum']=totalmusictime
    progressbarEndmusictime.configure(text='{}'.format(str(datetime.timedelta(seconds=totalmusictime))))
    def progressbarmusictick():
        currentmusiclength=mixer.music.get_pos()//1000
        progressbarmusic['value']=currentmusiclength
        progressbarStartmusictime.configure(text='{}'.format(str(datetime.timedelta(seconds=currentmusiclength))))
        progressbarmusic.after(2,progressbarmusictick)
    progressbarmusictick()


def pause():
    mixer.music.pause()
    screen.pausebutton.grid_remove()
    screen.resumebutton.grid()
    audiolabel.configure(text='paused..')
def resume():
    screen.resumebutton.grid_remove()
    screen.pausebutton.grid()
    mixer.music.unpause()
    audiolabel.configure(text='playing..')
def stop():
    mixer.music.stop()
    audiolabel.configure(text='stoped..')

def volumeup():
       vol= mixer.music.get_volume()
       mixer.music.set_volume(vol+0.05)
       progressbarVolumelabel.configure(text='{}%'.format(int(mixer.music.get_volume()*100)))
       progressbarVolume['value']=mixer.music.get_volume()*100
def volumedown():
        vol= mixer.music.get_volume()
        mixer.music.set_volume(vol-0.05)
        progressbarVolumelabel.configure(text='{}%'.format(int(mixer.music.get_volume ()*100)))
        progressbarVolume['value']=mixer.music.get_volume()*100


def mute():
 mixer.music.get_volume()
 mixer.music.set_volume(0)
def unmute():
    mixer.music.get_volume()
    mixer.music.set_volume(0.1)


def createwidthes():
    global audiolabel,    progressbarVolumelabel,    progressbarVolume,    progressbarlabel,progressbarmusic,progressbarEndmusictime,progressbarStartmusictime
    Tracklabel=Label(screen,text='Select Audio Track:',bg='lightsky blue',font=('arial',10,'italic bold'))
    Tracklabel.grid(row=0,column=0,)
    audiolabel=Label(screen,text='pause...',bg='lightsky blue',font=('arial',10,'italic bold'))
    audiolabel.grid(row=6,column=1)

    Tracklabel=Entry(screen,width=40,textvariable=audiotrack)
    Tracklabel.grid(row=0,column=1,columnspan=3)
    searchbutton=Button(screen,text='Search',font=('arial',8,'italic bold'),bg='SkyBlue1',bd=5,activebackground='gold',command=musicurl,width=5,compound=RIGHT,
                        )
    searchbutton.grid(row=0,column=5,padx=10,pady=10)

    stopbutton=Button(screen,text='stop',font=('arial',8,'italic bold'),bg='plum1',bd=5,activebackground='gold',command=stop)
    stopbutton.grid(row=7,column=0)

    playbutton=Button(screen,text='play',font=('arial',8,'italic bold'),bg='plum1',bd=5,activebackground='gold',command=play)
    playbutton.grid(row=7,column=1)

    screen.pausebutton=Button(screen,text='pause',font=('arial',8,'italic bold'),bg='plum1',bd=5,activebackground='gold',command=pause)
    screen.pausebutton.grid(row=7,column=2)

    screen.resumebutton=Button(screen,text='resume',font=('arial',8,'italic bold'),bg='plum1',bd=5,activebackground='gold',command=resume,)
    screen.resumebutton.grid(row=7,column=2)
    screen.resumebutton.grid_remove()

    volumeupbutton=Button(screen,text='volumme +',font=('arial',8,'italic bold'),bg='RoyalBlue1',bd=5,activebackground='gold',command=volumeup,width=10)
    volumeupbutton.grid(row=3,column=5)

    volumedownbutton=Button(screen,text='volume -',font=('arial',8,'italic bold'),bg='RoyalBlue2',bd=5,activebackground='gold',command=volumedown,width=10)
    volumedownbutton.grid(row=5,column=5)

    mutebutton=Button(screen,text='mute ',font=('arial',8,'italic bold'),bg='RoyalBlue1',bd=5,activebackground='gold',command=mute,width=10)
    mutebutton.grid(row=6,column=5,padx=20,pady=20)

    screen.unmutebutton=Button(screen,text='unmute',font=('arial',8,'italic bold'),bg='RoyalBlue1',bd=5,activebackground='gold',command=unmute,width=10)
    screen.unmutebutton.grid(row=7,column=5)

########################################################################
    progressbarlabel=Label(screen,text='',bg='blue',)
    progressbarlabel.grid(row=4,column=5,padx=10,pady=10)

    progressbarVolume=Progressbar(progressbarlabel,orient=VERTICAL,value=0,mode='determinate',length=150)
    progressbarVolume.grid(row=4,column=5,ipadx=5)
    progressbarVolumelabel=Label(progressbarlabel,bg='lightgrey',text='')
    progressbarVolumelabel.grid(row=4,column=5)
    ############################################33
    progressbarmusiclabel=Label(screen,text='',bg='blue',)
    progressbarmusiclabel.grid(row=5,column=1)

    progressbarStartmusictime=Label(screen,text='0:00:0',bg='blue',font=('arial',12,'italic bold'),width=5)
    progressbarStartmusictime.place(x=335,y=254,)
    progressbarEndmusictime=Label(screen,text='0:00:0',bg='blue',font=('arial',12,'italic bold'),width=5)
    progressbarEndmusictime.place(x=75,y=254)
    progressbarmusic=Progressbar(progressbarmusiclabel,orient=HORIZONTAL,value=0,mode='determinate',length=200)
    progressbarmusic.grid(row=5,column=1)





























mixer.init()
createwidthes()
screen.mainloop()
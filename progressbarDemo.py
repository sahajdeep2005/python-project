import tkinter as tk
from tkinter import ttk
import progressbar
# root window
root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar Demo')

root.grid()

# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='determinate',
    length=280
)
# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)


# start button
start_button = ttk.Button(
    root,
    text='Start',
    command=pb.start
)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# stop button
stop_button = ttk.Button(
    root,
    text='Stop',
    command=pb.stop
)
stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)


root.mainloop()
##
# #################
def createwidthes():
    global audiolabel
    Tracklabel=Label(screen,text='Select Audio Track:',bg='lightsky blue',font=('arial',10,'italic bold'))
    Tracklabel.grid(row=0,column=0)
    audiolabel=Label(screen,text='pause...',bg='lightsky blue',font=('arial',10,'italic bold'))
    audiolabel.place(x=,250y=330)
    Tracklabel=Entry(screen,width=40,textvariable=audiotrack)
    Tracklabel.place(x=160,y=30)
    searchbutton=Button(screen,text='Search',font=('arial',8,'italic bold'),bg='SkyBlue1',bd=5,activebackground='gold',command=musicurl,width=5,compound=RIGHT,
                        )
    searchbutton.place(x=430,y=30)

    stopbutton=Button(screen,text='stop',font=('arial',8,'italic bold'),bg='plum1',bd=5,activebackground='gold',command=stop)
    stopbutton.place(x=80,y=400)

    playbutton=Button(screen,text='play',font=('arial',8,'italic bold'),bg='plum1',bd=5,activebackground='gold',command=play)
    playbutton.place(x=400,y=400)

    screen.pausebutton=Button(screen,text='pause',font=('arial',8,'italic bold'),bg='plum1',bd=5,activebackground='gold',command=pause)
    screen.pausebutton.grid(padx=250,pady=400)

    screen.resumebutton=Button(screen,text='resume',font=('arial',8,'italic bold'),bg='plum1',bd=5,activebackground='gold',command=resume,)
    screen.resumebutton.grid(padx=250,pady=400)
    screen.resumebutton.grid_remove()

    valumeupbutton=Button(screen,text='valumme +',font=('arial',8,'italic bold'),bg='RoyalBlue1',bd=5,activebackground='gold',command=valumeup,width=10)
    valumeupbutton.place(x=370,y=180)

    volumedownbutton=Button(screen,text='volume -',font=('arial',8,'italic bold'),bg='RoyalBlue2',bd=5,activebackground='gold',command=valumedown,width=10)
    volumedownbutton.place(x=370,y=240)

    mute_button=Button(screen,text='mute ',font=('arial',8,'italic bold'),bg='RoyalBlue1',bd=5,activebackground='gold',command=mute,width=10)
    mute_button.place(x=400,y=350)

    unmutebutton=Button(screen,text='unmute',font=('arial',8,'italic bold'),bg='RoyalBlue1',bd=5,activebackground='gold',command=unmute,width=10)
    unmutebutton.place(x=400,y=300)

    progressbarlabel=Label(screen,text='',bg='blue',)
    progressbarlabel.place(x=480,y=230)
    progressbarVolume=Progressbar(progressbarlabel,orient=VERTICAL,value=0,mode='determinate',length=200)
    progressbarVolume.place(x=480,y=230)






































mixer.init()
createwidthes()
screen.mainloop(
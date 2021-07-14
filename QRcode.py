from tkinter import*
from tkinter import messagebox
import qrcode



screen=Tk()
screen.title('QR code')
screen.maxsize(width=450,height=250)
screen.minsize(width=465,height=250)
screen.configure(bg='powder blue')

def generate():
   name= Name_entry_box.get()
   id=ID_entery_box.get()
   message=Message_entery_box.get()
   web=website2.get()
   detail='name:'+name+'\n'+'Id:'+id+'\n'+'message:'+message+'\n'+'mail:sahajdeep8949@gmail.com''\n'+'website'+web
   qr = qrcode.QRCode(
       version=1,
       box_size=10,
       border=5)
   qr.add_data(detail,text)
   qr.make(fit=True)
   img = qr.make_image(fill='black', back_color='white',)
   img.save('QR code2.png')

#img = qrcode.make(detail)
   #type(img)
   #img.save("QR code.png")





def Quit_root():
    res=messagebox.askokcancel('notification','Are you sure you want to quit')
    if res==True:
        screen.destroy()

    else:
        pass
def clean():
    Name_entry_box.delete(0,END)
    ID_entery_box.delete(0,END)
    Message_entery_box.delete(0,END)
    website.delete(0,END)
def on_leavegenerate(s):
    generate.configure(bg='pink')
def on_entergenerate(s):
    generate.configure(bg='orange')

def on_leaveclear(s):
    clean.configure(bg='pink')
def on_enterclear(s):
    clean.configure(bg='orange')

def on_leaveQuit(s):
        Quit.configure(bg='pink')
def on_enterQuit(s):
    Quit.configure(bg='orange')



###################################33
QR_ID_label=Label(screen,text='Enter Your ID',font=('arial',13,'italic bold'),bg='powder blue',fg='red',width=17)
QR_ID_label.place(x=20,y=40)

QR_Name_label=Label(screen,text='Enter Your Name ',font=('arial',13,'italic bold'),bg='powder blue',fg='red',width=17)
QR_Name_label.place(x=20,y=80)

QR_Message_label=Label(screen,text='Enter Your message',font=('arial',13,'italic bold'),bg='powder blue',fg='red',width=17)
QR_Message_label.place(x=20,y=120)

website=Label(text=' website:',font=('arial',13,'italic bold'),bg='powder blue',fg='red',width=17)
website.place(x=20,y=220)

#website=Label(screen,text=notification,font=('arial',13,'italic bold'),bg='pink',width=27,)
#website.place(x=210,y=220)

###################################

website2=Entry(screen,text='',font=('arial',15,'italic bold'),bg='pink',width=22,bd=5)
website2.place(x=210,y=220)

ID_entery_box=Entry(screen,font=('arial',10,'italic bold'),bg='pink',bd=5,width=23)
ID_entery_box.place(x=280,y=40)

Name_entry_box=Entry(screen,font=('arial',10,'italic bold'),bg='pink',bd=5,width=23)
Name_entry_box.place(x=280,y=80)

Message_entery_box=Entry(screen,font=('arial',10,'italic bold'),bg='pink',bd=5,width=23)
Message_entery_box.place(x=280,y=120)

########################



generate=Button(screen,text='Generate',font=('arial',10,' bold'),bg='pink',bd=5,width=10,command=generate)
generate.place(x=30,y=170)


clean=Button(screen,text='clean',font=('arial',10,' bold'),bg='pink',bd=5,width=10,command=clean)
clean.place(x=190,y=170)


Quit=Button(screen,text='Quit',font=('arial',10,' bold'),bg='pink',bd=5,width=10,command=Quit_root)
Quit.place(x=350,y=170)
#######################################
generate.bind('<Enter>',on_entergenerate)
generate.bind('<Leave>',on_leavegenerate)

clean.bind('<Enter>',on_enterclear)
clean.bind('<Leave>',on_leaveclear)

Quit.bind('<Enter>',on_enterQuit)
Quit.bind('<Leave>',on_leaveQuit)

































screen.mainloop()
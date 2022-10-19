# ============= Import Library ============= #

from tkinter import Tk, Label, Frame
from datetime import datetime
from time import strftime

# ============= Main Window Config ============= #

WIN =  Tk()
WIN.maxsize(480, 120)
WIN.resizable(False, False)
WIN.configure(bg="black")
WIN.title("DIGITAL CLOCK") 

# ============= Definition ============= #

def stay_on_top():
    """ - Always Stay On Top - """
    WIN.lift()
    WIN.after(2000, stay_on_top)


def string_format_time():
    """ String Format Time (Time) """
    format_time = strftime("%H : %M : %S")
    label.config(text= format_time)
    label.after(1000, string_format_time)


def labels():

    label2=Label(frame, font=('Century Gothic',10),bg='#23262D',fg='#898D97',text='DAY')
    label2.place(x=392, y=80)

    label3=Label(frame, font=('Century Gothic',10),bg='#23262D',fg='#898D97',text='HOURS')
    label3.place(x=46, y=80)

    label4=Label(frame, font=('Century Gothic',10),bg='#23262D',fg='#898D97',text='MINUTES')
    label4.place(x=134, y=80)
 
    label5=Label(frame, font=('Century Gothic',10),bg='#23262D',fg='#898D97',text='SECONDS')
    label5.place(x=230, y=80)


# ============= String Format Time (Date) ============= #

a = datetime.today().strftime("%A")
b = (a.upper())
c = (b[0:3]) 

# ============= GUI Mapping ============= #

frame =  Frame(WIN, width=750, height=200, bg="#282C34")
frame.pack(expand=True)

label = Label(frame, font=("Century Gothic", 40), bg="#282C34", fg="#BFC4D3")
label.place(x= 32, y=15)

label1 = Label(frame, font=('Century Gothic',40), bg='#282C34', fg='#BFC4D3')
label1.config(text=c)
label1.place(x=358, y=15)

label1 = Label(frame, font=('Century Gothic',40), bg='#282C34', fg='#BFC4D3', text='|')
label1.place(x=300, y=10)

# ============= Call Function ============= #
labels()
string_format_time()

# ============= Call Main GUI ============= #

WIN.mainloop()

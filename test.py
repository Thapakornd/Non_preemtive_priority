import email
from tkinter import ttk
import tkinter
from tkinter.ttk import *
from tkinter import *
import time
from turtle import left, position, st, width
import pandas as pd

df = pd.read_excel("test11.xlsx")
proc = df.to_numpy().tolist()

window = Tk()
def sec():
    top = Toplevel()
    top.resizable(False,False)
    top.geometry("500x500+10+10")
    
    def start(bar_proc):
        while bar_proc['value'] < 100:
            bar_proc["value"] += 10
            time.sleep(1)
            my_canvas.update_idletasks()
            sec_frame.update_idletasks()
            mainframe.update_idletasks()
            top.update_idletasks()

    mainframe = Frame(top)
    mainframe.pack(fill=BOTH,expand="yes")

    my_canvas = Canvas(mainframe)
    my_canvas.pack(side=LEFT, fill=BOTH, expand="yes")

    my_scollbar = ttk.Scrollbar(mainframe, orient=VERTICAL, command=my_canvas.yview)
    my_scollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scollbar.set)
    my_canvas.bind("<Configure>", lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    sec_frame = Frame(my_canvas)
    sec_frame.pack()

    # Set number of process
    temp = []
    for p in proc:
        temp.append(p[0])
    temp.append(0)
    size_scroll = (len(temp) * 50) + 25 # <----- Set Scroll bar size

    # Create Scrollbar in frame
    my_canvas.create_window((0,0),window=sec_frame, anchor="nw",width=500,height=size_scroll)

    # Create process bar
    #for set in range(len(temp)):
    #Label(sec_frame, text=f"{temp[set]} ----- {temp[set]}").place(relx=0.45,y=set*50)
    bar_1 = Progressbar(sec_frame, orient=HORIZONTAL, mode="determinate",length=100)
    bar_1.place(relx=0.2,y=(50) + 25)
    #Label(sec_frame, text=f"{temp[set]}").place(relx=0.1, y = (set * 50) + 25)
    top.update_idletasks()
    start(bar_1)
    


text = StringVar()
percent = StringVar()

def start(bar_proc):
        while bar_proc['value'] < 350:
            time.sleep(0.1)
            bar_proc["value"] += 35
            window.update_idletasks()

#percentLabel = Label(window,textvariable=percent).pack()
texlabel = Label(window,textvariable=text).pack()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

button2 = Button(window, text="และทำไมคับ",command=lambda:start(bar)).pack()
button1 = Button(window, text="กดสิคับ",command=lambda:sec()).pack()

window.mainloop()
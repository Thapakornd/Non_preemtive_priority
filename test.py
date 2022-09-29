import email
from tkinter import ttk
import tkinter
from tkinter.ttk import *
from tkinter import *
import time
from turtle import left, position, width
import pandas as pd



df = pd.read_excel("test11.xlsx")
proc = df.to_numpy().tolist()

def start():
    tasks = 10
    x = 0
    while x < tasks:
        time.sleep(0.01)
        bar["value"] += 10
        x += 1
        percent.set(str((x/tasks)*100))
        text.set(str(x)+"/"+str(tasks)+" task completed")
        window.update_idletasks()

window = Tk()
def sec():
    top = Toplevel()
    top.resizable(False,False)
    top.geometry("500x500+10+10")
    
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
    for set in range(len(temp)):
        Label(sec_frame, text=f"{temp[set]} ----- {temp[set]}").place(relx=0.45,y=set*50)
        Progressbar(sec_frame, orient=HORIZONTAL, mode="determinate",length=350).place(relx=0.2,y=(set*50) + 25)
        Label(sec_frame, text=f"{temp[set]}").place(relx=0.1, y = (set * 50) + 25)
text = StringVar()
percent = StringVar()

percentLabel = Label(window,textvariable=percent).pack()
texlabel = Label(window,textvariable=text).pack()

bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

button = Button(window,text="download",command=start).pack()
button1 = Button(window, text="กดสิคับ",command=lambda:sec()).pack()

window.mainloop()
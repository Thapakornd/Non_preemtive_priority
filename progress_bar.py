from tkinter import *
from tkinter import ttk
import time
import os

root = Tk()
root.geometry("800x400")

def step(proc):
    while proc['value'] != 100:
        proc['value'] += 10
        root.update_idletasks()
        time.sleep(0.1)

num = [100,200,300,400,500]

def con():
    x = 100
    lenght_w = []
    for i in num:
        lenght_w = int(i / 2)
    my_proc = 10
    my_proc1 = []
    for row in range(my_proc):
        my_proc1[row] = ttk.Progressbar(root, orient=HORIZONTAL,
                    length=100,style='green.Horizontal.TProgressbar')
        my_proc1[row].place(relx=x,rely=0)
        x += 100
    
    for process in my_proc1:
        step(process)

def cmd():
    os.system("start cmd /k python Non_preem_prio.py")

s = ttk.Style()
s.theme_use('clam')
s.configure('green.Horizontal.TProgressbar',troughcolor='blue',background='red')
s.configure('red.Horizontal.TProgressbar',troughcolor='blue',background='green')

my_button = Button(root, text="Progress",command=lambda:cmd())
my_button.pack(pady=20)

root.mainloop()

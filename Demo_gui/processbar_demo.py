import tkinter as tk
from tkinter import ttk
from tkinter import *
import time

root = tk.Tk()
root.geometry("500x500")
root.resizable(0,0)

def step(proc,burst):
    slice_bar = int(100 / burst)
    while proc['value'] < 100:
        proc['value'] += slice_bar
        root.update_idletasks()
        time.sleep(0.01)

frame1 = ttk.Labelframe(root,text="Test")
frame1.place(relheight=1,relwidth=1)

my_canvas =

temp_list = []
for i in range(50):
    temp_list[i] = ttk.Progressbar(root,length=100,mode='determinate')
root.mainloop()
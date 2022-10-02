from this import d
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
        sec_frame.update_idletasks()
        time.sleep(0.01)

frame1 = ttk.Labelframe(root,text="Test")
frame1.place(relheight=0.3,relwidth=1)

frame2 = ttk.Labelframe(root, text="Text")
frame2.place(rely=0.5,x=30,relheight=0.3,relwidth=1)

my_canvas = Canvas(frame1)
my_canvas.place(relheight=1,relwidth=1)

xscorll = ttk.Scrollbar(frame1, orient='horizontal', command=my_canvas.xview)
xscorll.pack(side='bottom',fill='x')

my_canvas.configure(xscrollcommand=xscorll.set)
my_canvas.bind("<Configure>",lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

sec_frame = Frame(my_canvas)
sec_frame.place(relheight=1,relwidth=1)

my_canvas.create_window((0,0),window=sec_frame, anchor='nw',width=1600,height=1000)

temp_list = []
burst_t = [20,100,40,600,60,1000]

#temp_ = ttk.Progressbar(sec_frame,length=100,mode='determinate')
#temp_.place(x= 80 + 10,y = 50)
#temp_.pack()

text_1 = StringVar()
percent_text = []

for i in range(6):
    percent_text.append(i)
    process_label = ttk.Label(sec_frame, text=f"P{i+1}")
    process_label.place(x = ((i+1) * 220) - (i*70), y = 20)
    percent_text[i] = ttk.Label(sec_frame, text=f"{i} -------- {(i+1)*5}")
    percent_text[i].place(x = ((i+1) * 190) - (i*40),y=80)
    temp_list.append(i)
    temp_list[i] = ttk.Progressbar(sec_frame,length=150,mode='determinate')
    temp_list[i].place(x=(i+1) * 150,y = 50)
    #step(temp_list[i],burst_t[i])
    x = 1
    task = 150
    slice_bar = 100 / burst_t[i]
    while x <= burst_t[i]:
        time.sleep(0.01)
        temp_list[i]['value'] += slice_bar
        text_1.set(str(int(x)))
        x += 1
        root.update()
root.mainloop()
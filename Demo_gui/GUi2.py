import tkinter as tk
from tkinter import Button, Canvas, Frame, LabelFrame, ttk


root = tk.Tk()
root.geometry("800x600")
root.resizable(0,0)

frame2 = Frame(root)
frame2.place(relheight=1,relwidth=1)

my_canvas = Canvas(frame2)
my_canvas.place(relheight=1,relwidth=1)

scrollbar = tk.Scrollbar(frame2, orient='vertical',command=my_canvas.yview)
scrollbar.pack(side='right',fill='y')

my_canvas.configure(yscrollcommand=scrollbar.set)
my_canvas.bind('<Configure>',lambda e:my_canvas.configure(scrollregion=my_canvas.bbox('all')))

for i in range(50):
    Button(frame2,text=f"Test{i}").pack()

root.mainloop()
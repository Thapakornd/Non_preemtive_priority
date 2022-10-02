
import tkinter as tk
from tkinter import Canvas, Frame, Label, filedialog, ttk, messagebox
import pandas as pd
import time

root = tk.Tk()
root.geometry("800x600")
root.iconbitmap(r'icons.ico')
root.title("CPU scheduling Non-Preemtive-Priority v1.0")
root.resizable(0,0)

# Frame Treeview Excel data
frame1 = tk.LabelFrame(root, text="Excel Data",font=('',16,'bold'))
frame1.place(height=300,width=380,x=10)

# Frame Treeview Excute data
frame2 = tk.LabelFrame(root, text="Excute File",font=('',16,'bold'))
frame2.place(height=300,width=380,x=410)

# Style treeview
s = ttk.Style()
s.theme_use('alt')
s.configure("Treeview",background='white',foreground ='black')
s.map('Treeview',background=[('selected','green')])

# Frame for open file dialog
file_frame = tk.LabelFrame(root, text="Open File",font=('',16,'bold'))
file_frame.place(height=100, width=380, x=10, rely=0.5)

# Frame for Information CPU comput
comput_frame = tk.LabelFrame(root, text="Comput Information",font=('',16,'bold'))
comput_frame.place(height=100, width=380, x=410, rely=0.5)

# Frame for Progress Bar
process_frame = tk.LabelFrame(root, text="Process Bar",font=('',16,'bold'))
process_frame.place(height=185,width=780, x=10, rely=0.67)

# Button search file
button_search = tk.Button(file_frame, text="Browse a file",command=lambda: file_dialog(),bg='#aa9797',bd=3)
button_search.place(rely=0.45,relx=0.15)

# Button Load file to excute
button_excute = tk.Button(file_frame, text="Load file", command=lambda: load_file(),bg='#aa9797',bd=3)
button_excute.place(rely=0.45, relx=0.45)

# Button Simulate Progress Bar
button_simu = tk.Button(file_frame, text="Simulate File",command=lambda: simulate(),bg='#aa9797',bd=3)
button_simu.place(rely=0.45, relx=0.7)

# File name selected
label_file = ttk.Label(file_frame, text="No File Selected")
label_file.place(relx=0.1,rely=0)

# Treeview
# ---------- Excel Data ------------
tree_excel = ttk.Treeview(frame1)
tree_excel.place(relheight=1,relwidth=1)

# ---------- Excute Data ------------
tree_excute = ttk.Treeview(frame2)
tree_excute.place(relheight=1,relwidth=1)

# Scrollbarr set up Frame 1
excel_scroll_y = tk.Scrollbar(frame1, orient="vertical", command=tree_excel.yview)
excel_scroll_x = tk.Scrollbar(frame1, orient="horizontal", command=tree_excel.xview)

tree_excel.configure(xscrollcommand=excel_scroll_x.set, yscrollcommand=excel_scroll_y.set)
excel_scroll_x.pack(side='bottom',fill="x")
excel_scroll_y.pack(side='right',fill='y')

# Scrollbar set up Frame 2
ex_scroll_y = tk.Scrollbar(frame2, orient="vertical", command=tree_excute.yview)
ex_scroll_x = tk.Scrollbar(frame2, orient="horizontal", command=tree_excute.xview)

tree_excute.configure(xscrollcommand=ex_scroll_x.set,yscrollcommand=ex_scroll_y.set)
ex_scroll_x.pack(side='bottom',fill="x")
ex_scroll_y.pack(side='right',fill='y')

# Function to excute program
def file_dialog():  # <-- Select path file to excute
    filename = filedialog.askopenfilename(initialdir="/",
                title="Select a File",filetypes=(("xlsx files","*.xlsx"),("all files","*.*")))
    label_file['text'] = filename

def clear_data(tree):  # <-- Clear data on treeview
    tree.delete(*tree.get_children())
    for widget in comput_frame.winfo_children():
        widget.destroy()

def simulate(): # <-- Simulate Progress Bar each process

    for fam in process_frame.winfo_children():
        fam.destroy()

    try: # <-- Check Value in load_file.proc
        process_bar = []
        process_bar = load_file.proc
    except AttributeError:
        messagebox.showerror("Information","Error value not found.")
        return None

    def stepup(bar,busrt): # <-- Function run process bar
        slice_bar = 100 / busrt
        x = 1
        while x <= busrt:
            bar['value'] += slice_bar
            burst_text.config(text=str(x) + "/" + str(busrt))
            x += 1
            root.update()
            time.sleep(0.008)
        
    # Set templete to scroll bar
    temp = (len(process_bar) * 150) + 400
    my_canvas = Canvas(process_frame)
    my_canvas.place(relheight=1,relwidth=1)

    my_scrollbar = tk.Scrollbar(process_frame, orient="horizontal",command=my_canvas.xview)
    my_scrollbar.pack(side='bottom',fill='x')

    my_canvas.configure(xscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e: my_canvas.configure(scrollregion=my_canvas.bbox('all')))

    sec_frame = Frame(my_canvas)
    sec_frame.place(relheight=1,relwidth=1)

    # Set Scroll bar horizontal
    my_canvas.create_window((0,0),window=sec_frame ,anchor='nw',width=temp,height=1800)
    
    # Set coloum[0] == " " size : 150 for space
    Label(sec_frame,text="### Assign time : 1 sec/burst time ###").grid(row=0,column=0)
    Label(sec_frame,text="Start  ------->",font=('',12,'bold')).grid(row=2,column=0)
    sec_frame.grid_columnconfigure(0, minsize=150)

    # Create Process Bar Part
    for i in range(len(process_bar)):

        if process_bar[i][0] == 'None':  # <-- Check value 
            pas_col = 'red'
            text_a = 'red'
            bur_txt = 'red'
        else:
            pas_col = 'green'
            text_a = 'black'
            bur_txt = 'black'

        # Process name 
        process_label = ttk.Label(sec_frame, text=f"{process_bar[i][0]}",font=('',12,'bold'),foreground=pas_col,background='white')
        process_label.grid(row=1,column=1+i)

        # Progress bar
        proc_bar = ttk.Progressbar(sec_frame,length=150,orient='horizontal',mode='determinate')
        proc_bar.grid(row=2,column=1+i)

        # Time text
        text_arr = ttk.Label(sec_frame, text=f"{process_bar[i][2]} |--->--->--->---| {process_bar[i][3]}",font=('',9,''),foreground=text_a)
        text_arr.grid(row=3,column=1+i)

        # Burst Text
        burst_text =  ttk.Label(sec_frame, text="0",foreground=bur_txt,font=('',12,'bold'))
        burst_text.grid(row=4,column=1+i)

        sec_frame.grid_columnconfigure(i+1, minsize=150)
        for row in range(3):
            sec_frame.grid_rowconfigure(row, minsize=30)

        stepup(proc_bar,process_bar[i][1])  # <--- Function run bar
        root.update()  # <--- Update Screen
    
    Label(sec_frame,text="END of Process",font=('',12,'bold')).grid(row=2,column=i+2)
    sec_frame.grid_columnconfigure(i+2, minsize=150)

def load_file(): # <-- Loadfile to excute
    file_path = label_file['text']
    try:
        df = pd.read_excel(file_path)
    except:
        messagebox.showerror("Information","Error pls try again!")
        return None

    clear_data(tree_excel)  # <--- Clear Before Data
    clear_data(tree_excute)
    
    # Create Excel Date into treeview(LEFT)
    r_row = df.to_numpy().tolist()
    tree_excel["column"] = list(df.columns)
    tree_excel["show"] = "headings"
    for col in tree_excel['column']:
        tree_excel.column(col, minwidth=90,width=90,anchor='center')

    for column in tree_excel['column']:
        tree_excel.heading(column, text=column, anchor='center')            

    tree_excel.tag_configure('grey',background='lightgrey')
    tree_excel.tag_configure('normal',background='white')
    row_num = 1    
    for row in r_row: # <-- Check for color even, odd row
        if row_num % 2 == 0:
            my_tag = 'grey'
        else:
            my_tag = 'normal' 
        tree_excel.insert("","end",values=row,tags=my_tag)
        row_num += 1

    proc = df.to_numpy().tolist() # <-- Set value process to calculate
    totalprocess = len(proc)

    # Sort arrival time each process
    def sort_proc():
        temp = []
        for j in range(totalprocess):
            for i in range(0,totalprocess-j-1,1):
                if proc[i][2] > proc[i+1][2]: # swap value p[i] and p[i+1]
                    temp = proc[i]
                    proc[i] = proc[i+1]
                    proc[i+1] = temp

    # Sort Priority each arrival time
    def sort_prio(b_t,p_t):
        # Check value while arrival time
        stk = 0
        for i in range(p_t,totalprocess):
            if proc[i][2] <= b_t:
                stk += 1
        
        for i in range(stk): # <---- swap Process with priority
            for j in range(p_t,stk-i,1):
                if proc[j][3] > proc[j+1][3]:
                    temp = proc[j]
                    proc[j] = proc[j+1]
                    proc[j+1] = temp

    s_time = [] # <------ Comput time each process
    p_t = 0  # <---- Set Process computed
    taround_t = []  # <------- TurnAround Time
    wat_t = []  # <--------- Waiting time
    output = []  # <-------- Process Bar
    burst_t = 0  # <-------- total Burst_time 
    t = 0  # <-------- Time running
    sum_wat = 0  # <--- Sum waiting time
    sum_tr = 0  # <--- Sum turn time

    for i in range(totalprocess):
        burst_t += proc[i][1]

    # Function sort arrival time    
    sort_proc()   
    s_time.append(0) # <-- Set first time at 0
    while True:
        if proc[p_t][2] <= t:  # <-- Check Arrival time
            if t != s_time[-1]:  # <-- Check before arrival to cal
                s_time.append(t)
                # Output append "None" when no process in previos timm:t
                output.append(["None",t-s_time[-2],s_time[-2],s_time[-1]])
            s_time.append(proc[p_t][1] + s_time[-1])  # <-- Burst time add to time
            output.append([proc[p_t][0],proc[p_t][1],s_time[-2],s_time[-1]])
            taround_t.append(s_time[-1]-proc[p_t][2])
            wat_t.append(taround_t[p_t]-proc[p_t][1])
            sum_tr += taround_t[p_t]
            sum_wat += wat_t[p_t]
            sort_prio(s_time[-1],p_t)  # Sort priority at time
            p_t += 1   # <-- Assign process complete to break
            t = s_time[-1]  # t == last time comput
        if p_t == totalprocess:
            break
        # Check 't' if next Process arrival time > 't' + 1 sec
        if proc[p_t][2] != s_time[-1] and proc[p_t][2] > s_time[-1]:
            t += 1

    # Add value to process
    for wt in range(len(wat_t)):
        proc[wt].append(wat_t[wt])
        proc[wt].append(taround_t[wt])
        
    # Write data to Excute frame
    temp_tolist = list(df.columns)
    temp_tolist.append("Waiting")
    temp_tolist.append("Turnaround")
    tree_excute["column"] = temp_tolist
    tree_excute["show"] = "headings"
    for col in tree_excute["column"]:
        tree_excute.column(col, width=60,minwidth=60,anchor='center')
    for column in tree_excute["column"]:
        tree_excute.heading(column, text=column, anchor='center')
    
    # Set up color in even row
    tree_excute.tag_configure('blue',background='lightblue')
    tree_excute.tag_configure('normal',background='white')
    row_num = 1
    for row in proc:
        if row_num % 2 == 0:
            my_tag = 'blue'
        else:
            my_tag = 'normal'
        tree_excute.insert("","end",values=row,tags=my_tag)
        row_num += 1
    
    # Information after comput program
    a_t_r = ttk.Label(comput_frame, text=f"Avg Turnaround time :    {sum_tr / totalprocess:.2f}",)
    a_w_t = ttk.Label(comput_frame, text=f"Avg Waiting time :    {sum_wat / totalprocess:.2f}")
    t_p = ttk.Label(comput_frame, text=f"Throughput :    {totalprocess / s_time[-1]:.2f} process/sec")
    cpu_un = ttk.Label(comput_frame, text=f"CPU utilization :    {burst_t / s_time[-1] * 100:.2f}%")

    # Grid item
    a_w_t.grid(row=3,column=1)    
    a_t_r.grid(row=1,column=1)
    cpu_un.grid(row=3,column=3)
    t_p.grid(row=1,column=3)
    
    # Spacing
    comput_frame.rowconfigure(0,minsize=10)
    comput_frame.rowconfigure(3,minsize=30)
    comput_frame.columnconfigure(2,minsize=20)
    comput_frame.columnconfigure(0,minsize=10)

    # Copy value of process to sim in simulate
    load_file.proc = output

root.mainloop()

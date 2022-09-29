import tkinter as tk
from tkinter import CENTER, filedialog, ttk, messagebox
import pandas as pd
import os

root = tk.Tk()
root.geometry("800x500")
root.resizable(0,0)

# Frame for Treeview
frame1 = tk.LabelFrame(root, text="Excel Data")
frame1.place(height=400,width=400)

frame2 = tk.LabelFrame(root, text="Comput process")
frame2.place(height=400,width=400,x=400,rely=0)

frame3 = tk.LabelFrame(root, text="Infomation of CPU")
frame3.place(height=200,width=800,relx=0,rely=0.7)

# Frame for for open file dialog
file_frame = tk.LabelFrame(root, text="Open File")
file_frame.place(height=100, width=800,relx=0,rely=0.5)

# Button
button1 = tk.Button(file_frame, text="Browse a file",command=lambda:file_dialog())
button1.place(rely=0.5,relx=0.1)

# Load file butt
button2 = tk.Button(file_frame, text="Load File",command=lambda: load_excel_data())
button2.place(rely=0.5,relx=0.3)

# Excute file butt
button3 = tk.Button(file_frame, text="Excute File",command=lambda:excute_data())
button3.place(rely=0.5, relx=0.5)

# CPUsimulate
button4 = tk.Button(file_frame, text="Simulate CPU",command=lambda:simulate())
button4.place(rely=0.5, relx=0.7)

label_file = ttk.Label(file_frame, text="No file Selected")
label_file.place(rely=0,relx=0)

# Treeview
tree = ttk.Treeview(frame1)
tree.place(relheight=1,relwidth=1)
tree_x = ttk.Treeview(frame2)
tree_x.place(relheight=1,relwidth=1)

# Scrollbar set up
tree_s_y = tk.Scrollbar(frame1, orient="vertical", command=tree.yview)
tree_s_x = tk.Scrollbar(frame1, orient="horizontal", command=tree.xview)
tree_s_y_1 = tk.Scrollbar(frame2, orient="vertical", command=tree.yview)
tree_s_x_1 = tk.Scrollbar(frame2, orient="horizontal", command=tree.yview)

tree.configure(xscrollcommand=tree_s_x.set, yscrollcommand=tree_s_y.set)
tree_x.configure(xscrollcommand=tree_s_x_1.set, yscrollcommand=tree_s_y_1.set)

tree_s_x.pack(side="bottom",fill="x")
tree_s_y.pack(side="right",fill="y")
tree_s_x_1.pack(side="bottom",fill="x")
tree_s_y_1.pack(side="right",fill="y")

def excute_data():

    file_path = label_file["text"]
    try:
        excute_file = pd.read_excel(r"{}".format(file_path))
    except:
        messagebox.showerror("Information","Something went wrong try again.")
        return None

    # Set up file to cal
    proc = excute_file.to_numpy().tolist()
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
            for j in range(p_t,stk-i+p_t-1,1):
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
    sum_wat = 0
    sum_tr = 0

    # Calculate all burst time
    for i in proc:
        burst_t += i[1]

    # Function sort arrival time    
    sort_proc()    
    s_time.append(0)
    while True:
        if proc[p_t][2] <= t:
            if t != s_time[-1]:
                s_time.append(t)
                output.append(["None",t-s_time[-2]])
            s_time.append(proc[p_t][1] + s_time[-1])
            output.append([proc[p_t][0],proc[p_t][1],s_time[-2],s_time[-1]])
            taround_t.append(s_time[-1]-proc[p_t][2])
            wat_t.append(taround_t[p_t]-proc[p_t][1])
            sum_tr += taround_t[p_t]
            sum_wat += wat_t[p_t]
            p_t += 1
            sort_prio(s_time[-1],p_t)
            t = s_time[-1]
        if p_t == totalprocess:
            break
        if proc[p_t][2] != s_time[-1] and proc[p_t][2] > s_time[-1]:
            t += 1

    print("\n     Process   \t    Bursttime\t   Arrivaltime\t     Priority\t     Waiting \t   Turnaround")
    for i in range(totalprocess):
        print(f"\t{proc[i][0]} \t|\t{proc[i][1]} \t|\t{proc[i][2]} \t|\t{proc[i][3]} \t|\t{wat_t[i]} \t|\t{taround_t[i]}")

    print(f"\nAvg Turnaround time : {sum_tr / totalprocess}")
    print(f"Avg Waiting time : {sum_wat / totalprocess}")
    print(f"Throughput : {totalprocess / s_time[-1]:.2f} process/sec")
    print(f"CPU utilization : {burst_t / s_time[-1] * 100:.2f}")

    # Write data to Treeview
    temp_to_list = list(excute_file.columns)
    temp_to_list.append("Waiting")
    temp_to_list.append("Turnaround")
    tree_x["column"] = temp_to_list
    tree_x["show"] = "headings"
    for col in tree_x["column"]:
        tree_x.column(col, width="1",anchor=CENTER)
    for column in tree_x["column"]:
        tree_x.heading(column, text=column,anchor=CENTER)
    for row in proc:
        tree_x.insert("","end",values=row)

    # Information output of CPU schedul
    label_avg_turn = tk.Label(frame3, text=f"Avg Turnaround Time : {sum_tr / totalprocess}")
    label_avg_wait = tk.Label(frame3, text=f"Avg Waiting Time : {sum_wat / totalprocess}")
    label_thrput = tk.Label(frame3, text=f"Throughput : {totalprocess / s_time[-1]:.2f} process/sec")
    label_cpu_un = tk.Label(frame3, text=f"CPU utilization : {burst_t / s_time[-1] * 100:.2f}")
    
    label_avg_turn.pack()
    label_avg_wait.pack()
    label_thrput.pack()
    label_cpu_un.pack()
    
def simulate():
    os.system("start cmd /k python Non_preem_prio.py")
def file_dialog():
    filename = filedialog.askopenfilename(initialdir="/",
                title="Select a File",filetypes=(("xlsx files","*.xlsx"),("ALL Files","*.*")))
    label_file["text"] = filename

def load_excel_data():
    file_path = label_file["text"]
    try:
        excel_file = r"{}".format(file_path)
        re_excel = pd.read_excel(excel_file)
    except:
        messagebox.showerror("Information","The file you have chosen")
        return None

    clear_data(tree)
    tree["column"] = list(re_excel.columns)
    tree["show"] = "headings"
    for col in tree["column"]:
        tree.column(col, width="1",anchor=CENTER)

    for column in tree["column"]:
        tree.heading(column, text=column,anchor=CENTER)
    r_rows = re_excel.to_numpy().tolist()
    for row in r_rows:
        tree.insert("","end",values=row)    
    return None
        
def clear_data(info_tree):
    info_tree.delete(*info_tree.get_children())

# Function Calculate CPU scheduling

root.mainloop()
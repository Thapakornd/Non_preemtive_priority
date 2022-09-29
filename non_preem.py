import tkinter as tk
from tkinter import CENTER, filedialog, ttk, messagebox
import pandas as pd

root = tk.Tk()
root.geometry("800x800")
root.resizable(0,0)

# Frame for Treeview
frame1 = tk.LabelFrame(root, text="Excel Data")
frame1.place(height=400,width=400)

frame2 = tk.LabelFrame(root, text="Comput process")
frame2.place(height=400,width=400,x=400,rely=0)

# Frame for for open file dialog
file_frame = tk.LabelFrame(root, text="Open File")
file_frame.place(height=100, width=800,relx=0,rely=0.5)

# Button
button1 = tk.Button(file_frame, text="Browse a file",command=lambda:file_dialog())
button1.place(rely=0.5,relx=0.1)

button2 = tk.Button(file_frame, text="Load File",command=lambda: load_excel_data())
button2.place(rely=0.5,relx=0.3)

label_file = ttk.Label(file_frame, text="No file Selected")
label_file.place(rely=0,relx=0)

# Treeview
tree = ttk.Treeview(frame1)
tree.place(relheight=1,relwidth=1)

tree_s_y = tk.Scrollbar(frame1, orient="vertical", command=tree.yview)
tree_s_x = tk.Scrollbar(frame1, orient="horizontal", command=tree.xview)
tree.configure(xscrollcommand=tree_s_x.set, yscrollcommand=tree_s_y.set)
tree_s_x.pack(side="bottom",fill="x")
tree_s_y.pack(side="right",fill="y")

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

    clear_data()
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
        
def clear_data():
    tree.delete(*tree.get_children())
root.mainloop()
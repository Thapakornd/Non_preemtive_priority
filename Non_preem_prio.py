
from this import d
import time
from alive_progress import alive_bar
import pandas as pd  # <------ import pandas

# Read file from excel and get value
dic = pd.read_excel('test11.xlsx')
proc = list(dic.values)
totalprocess = len(proc)
burst_t = 0

for i in proc:
    burst_t += i[1]

# Sort arrival time each process
def sort_proc():
    temp = []
    for j in range(totalprocess):
        for i in range(0,totalprocess-j-1,1):
            if proc[i][2] > proc[i+1][2]: # swap value p[i] and p[i+1]
                temp = proc[i]
                proc[i] = proc[i+1]
                proc[i+1] = temp
    return proc

# Sort Priority each arrival time
def sort_prio(b_t):
    # Check value while arrival time

    stk = 0
    arr_t = []
    for i in range(totalprocess):
        if proc[i][2] <= b_t:
            stk += 1
    
    for i in range(stk): # <---- swap Process with priority
        for j in range(0,stk-i,+1):
            if proc[j][3] > proc[j+1][3]:
                temp = proc[j]
                proc[j] = proc[j+1]
                proc[j+1] = temp

def progress_bar(st,end,val):
    print(f"\t\t{st} -------- {end}")
    with alive_bar(end,title=f"{val}") as bar:
        for i in range(end):
            time.sleep(0.001)
            bar()

def find_va():
    s_time = [] # <------ Comput time each process
    tr_t = [0] * totalprocess   # <------ Turn around time each process
    wt = [0] * totalprocess   # <------ Waiting time each process
        # <------ Set P1 start 0 
    p_t = 0  # <---- Set Process computed
    sum_wt = 0
    sum_tr = 0
    output = []

    # Function sort arrival time    
    sort_proc()
    t = 0
    first_p = True
    s_time.append(0)
    while burst_t != 0:
        if proc[0][2] <= t:
            s_time.append(proc[0][1] + s_time[-1])
            output.append([proc[0][1],s_time[-2],s_time[-1]])
            proc.pop(0)

        


            
                        

    print("\nProcess \tBursttime \tArrivaltime \tPriority \tWaiting \tTurnaround")
    for i in range(totalprocess):
        print("{} \t\t{} \t\t{} \t\t{} \t\t{} \t\t{}".format(proc[i][0],proc[i][1],proc[i][2],proc[i][3],wt[i],tr_t[i]))
    print("\n\nAvg waiting time : {:.2f}".format(sum_wt))
    print("Avg turnaround time : {:.2f}".format(sum_tr))
    print("Throughput : {:.2f} process/sec\n".format(totalprocess / (s_time[-1])))


# Calculate queue non-preem-prioriy
find_va()

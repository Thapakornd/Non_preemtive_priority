
import time
from alive_progress import alive_bar
import pandas as pd  # <------ import pandas

# Read file from excel and get value
dic = pd.read_excel('test11.xlsx')
proc = list(dic.values)
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
    arr_t = []
    for i in range(p_t,totalprocess):
        if proc[i][2] < b_t:
            stk += 1
    
    for i in range(stk): # <---- swap Process with priority
        for j in range(p_t,stk-i,+1):
            if proc[j][3] > proc[j+1][3]:
                temp = proc[j]
                proc[j] = proc[j+1]
                proc[j+1] = temp

    for i in range(p_t,stk,1):
        arr_t.append(proc[i])

    return arr_t

def progress_bar(s_t,val,x):
    print(f"\t\t{s_t[x]} -------- {s_t[x+1]}")
    with alive_bar(s_t[x+1],title=f"{val}") as bar:
        for i in range(s_t[x+1]):
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
    
    # Function sort arrival time    
    sort_proc()

    i = 0
    first_1 = 0
    while True:
        if first_1 == 0:
            s_time.append(i)
            if proc[0][2] == 0:
                s_time.append(i+proc[0][1])
                p_t += 1
                progress_bar(s_time,proc[0][0],0)
                temp_re = sort_prio(i+proc[0][1],p_t)
            else:
                s_time.append(proc[0][2])
                p_t += 1
                progress_bar(s_time,"",0)
                s_time.append(s_time[1] + proc[0][1])
                progress_bar(s_time,proc[0][0],1)
                temp_re = sort_prio(s_time[1] + proc[0][1],p_t)
            first_1 += 1
        elif temp_re[0][2] == i:
            if s_time[-1] == i:
                s_time
            else:
                pass      
        i += 1
        

    print("\nProcess \tBursttime \tArrivaltime \tPriority \tWaiting \tTurnaround")
    for i in range(totalprocess):
        print("{} \t\t{} \t\t{} \t\t{} \t\t{} \t\t{}".format(proc[i][0],proc[i][1],proc[i][2],proc[i][3],wt[i],tr_t[i]))
    print("\n\nAvg waiting time : {:.2f}".format(sum_wt))
    print("Avg turnaround time : {:.2f}".format(sum_tr))
    print("Throughput : {:.2f} process/sec\n".format(totalprocess / (s_time[-1])))


# Calculate queue non-preem-prioriy
find_va()

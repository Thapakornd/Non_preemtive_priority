import time
from alive_progress import alive_bar
import pandas as pd  # <------ import pandas

# Read file from excel and get value
dic = pd.read_excel('test.xlsx')
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
    for i in range(p_t,totalprocess):
        if proc[i][2] < b_t:
            stk += 1
    
    for i in range(stk): # <---- swap Process with priority
        for j in range(p_t,stk-i,+1):
            if proc[j][3] > proc[j+1][3]:
                temp = proc[j]
                proc[j] = proc[j+1]
                proc[j+1] = temp

def find_va():
    s_time = [] # <------ Comput time each process
    tr_t = [0] * totalprocess   # <------ Turn around time each process
    wt = [0] * totalprocess   # <------ Waiting time each process
    s_time.append(0)  # <------ Set P1 start 0 
    p_t = 0  # <---- Set Process computed
    sum_wt = 0
    sum_tr = 0

    # Function sort arrival time    
    sort_proc()

    cpu_un = 0
    for i in range(totalprocess):
        cpu_un += proc[i][1]
    i = 0
    x = 0
    while True:
        if proc[x][2] == i:
            s_time.append(i)
            s_time.append(i+proc[x][1])
            if proc[x][1] == proc[-1][1]:
                break
            p_t += 1
            sort_prio(s_time[x],p_t)
            x += 1
        i += 1

    # CPU untilization
    cpu_un = (cpu_un / s_time[-1]) * 100 

    # Output
    '''for i in range(totalprocess):
        print(f"\t\t{s_time[i]} ------- {s_time[i+1]}")
        with alive_bar(proc[i][1],title=f"{proc[i][0]}") as bar:
            for x in range(proc[i][1]):
                time.sleep(0.001)
                bar()
    '''
    print("\nProcess \tBursttime \tArrivaltime \tPriority \tWaiting \tTurnaround")
    for i in range(totalprocess):
        print("{} \t\t{} \t\t{} \t\t{} \t\t{} \t\t{}".format(proc[i][0],proc[i][1],proc[i][2],proc[i][3],wt[i],tr_t[i]))
    #print("\n\nAvg waiting time : {:.2f}".format(sum_wt))
    #print("Avg turnaround time : {:.2f}".format(sum_tr))
    #print("Throughput : {:.2f} process/sec\n".format(totalprocess / (s_time[-1])))


# Calculate queue non-preem-prioriy
find_va()

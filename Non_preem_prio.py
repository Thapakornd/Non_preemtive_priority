import time
from alive_progress import alive_bar
import pandas as pd  # <------ import pandas

# Read file from excel and get value
dic = pd.read_excel('test.xlsx')
proc = list(dic.values)
totalprocess = len(proc)
# Set time comput is 1 ms 
comput_t = 0.001 

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
    s_time = [0] * (totalprocess+1)  # <------ Comput time each process
    tr_t = [0] * totalprocess   # <------ Turn around time each process
    wt = [0] * totalprocess   # <------ Waiting time each process
    s_time[0] = 0  # <------ Set P1 start 0 
    p_t = 0  # <---- Set Process computed
    sum_wt = 0
    sum_tr = 0
    
    # Function sort arrival time    
    sort_proc()

    for i in range(totalprocess):
        # Function create value each process
        s_time[i+1] = proc[i][1] + s_time[i]
        tr_t[i] = s_time[i+1] - proc[i][2]
        wt[i] = tr_t[i] - proc[i][1]
        p_t =+ 1
        sum_wt = sum_wt + wt[i] 
        sum_tr = sum_tr + tr_t[i]                  
        sort_prio(s_time[i+1],p_t)   # <---- Get value to sort prioriy

        # Avg of waiting time and turn around time
        sum_wt = sum_wt / totalprocess
        sum_tr = sum_tr / totalprocess

    # Output
    for i in range(totalprocess):
        print(f"\t\t{s_time[i]} ------- {s_time[i+1]}")
        with alive_bar(proc[i][1],title=f"{proc[i][0]}") as bar:
            for x in range(proc[i][1]):
                time.sleep(comput_t)
                bar()

    print("\nProcess \tBursttime \tArrivaltime \tPriority \tWaiting \tTurnaround")
    for i in range(totalprocess):
        print("{} \t\t{} \t\t{} \t\t{} \t\t{} \t\t{}".format(proc[i][0],proc[i][1],proc[i][2],proc[i][3],wt[i],tr_t[i]))
    print("\n\nAvg waiting time : {:.2f}".format(sum_wt))
    print("Avg turnaround time : {:.2f}".format(sum_tr))
    print("CPU utilization : 100%")
    print("Throughput : {:.2f} process/sec\n".format(totalprocess / (s_time[-1] * comput_t)))


# Calculate queue non-preem-prioriy
find_va()


import time
from alive_progress import alive_bar
import pandas as pd  # <------ import pandas

# Read file from excel and get value
dic = pd.read_excel("test11.xlsx")
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
        if proc[i][2] <= b_t:
            stk += 1
    
    for i in range(stk): # <---- swap Process with priority
        for j in range(p_t,stk-i+p_t-1,1):
            if proc[j][3] > proc[j+1][3]:
                temp = proc[j]
                proc[j] = proc[j+1]
                proc[j+1] = temp

def find_va():
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

    print("\n\t---------Process bar---------\n")
    for i in range(len(output)):
        print(f"\t\t {s_time[i]} ------- {s_time[i+1]}")
        with alive_bar(output[i][1],title=output[i][0]) as bar:
            for x in range(output[i][1]):
                time.sleep(0.001)
                bar()

    print("\n     Process   \t    Bursttime\t   Arrivaltime\t     Priority\t     Waiting \t   Turnaround")
    for i in range(totalprocess):
        print(f"\t{proc[i][0]} \t|\t{proc[i][1]} \t|\t{proc[i][2]} \t|\t{proc[i][3]} \t|\t{wat_t[i]} \t|\t{taround_t[i]}")

    print(f"\nAvg Turnaround time : {sum_tr / totalprocess}")
    print(f"Avg Waiting time : {sum_wat / totalprocess}")
    print(f"Throughput : {totalprocess / s_time[-1]:.2f} process/sec")
    print(f"CPU utilization : {burst_t / s_time[-1] * 100:.2f}")

# Calculate queue non-preem-prioriy

find_va()


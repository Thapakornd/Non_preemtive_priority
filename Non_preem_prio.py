
from this import d
import time
from alive_progress import alive_bar
import pandas as pd  # <------ import pandas

# Read file from excel and get value
dic = pd.read_excel('Book1.xlsx')
proc = list(dic.values)
totalprocess = len(proc)

# Sort arrival time each process
def sort_proc():
    temp = []
    for j in range(len(proc)):
        for i in range(0,len(proc)-j-1,1):
            if proc[i][2] > proc[i+1][2]: # swap value p[i] and p[i+1]
                temp = proc[i]
                proc[i] = proc[i+1]
                proc[i+1] = temp
    return proc

# Sort Priority each arrival time
def sort_prio(b_t,p_t):
    # Check value while arrival time
    stk = 0
    for i in range(p_t,len(proc)):
        if proc[i][2] <= b_t:
            stk += 1
    
    for i in range(stk): # <---- swap Process with priority
        for j in range(p_t,stk-i+p_t-1,1):
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
    burst_t = 0

    for i in proc:
        burst_t += i[1]

    # Function sort arrival time    
    sort_proc()
    t = 0
    first_p = True
    s_time.append(0)
    while True:
        if proc[p_t][2] <= t:
            if t != s_time[-1]:
                s_time.append(t)
            s_time.append(proc[p_t][1] + s_time[-1])
            output.append([proc[p_t][0],proc[p_t][1],s_time[-2],s_time[-1]])
            burst_t = burst_t - proc[p_t][1]
            p_t += 1
            sort_prio(s_time[-1],p_t)
            t = s_time[-1]
        if burst_t == 0:
            break
        if proc[p_t][2] != s_time[-1] and proc[p_t][2] > s_time[-1]:
            t += 1

            
    print("\nProcess \tBursttime \tArrivaltime \tPriority \tWaiting \tTurnaround")
    for i in range(totalprocess):
        print("{} \t\t{} \t\t{} \t\t{}".format(output[i][0],output[i][1],output[i][2],output[i][3]))

    for i in output:
        with alive_bar(i[1],title=i[0]) as bar:
            for x in range(i[1]):
                time.sleep(0.001)
                bar()

    print(s_time)
    #print("\n\nAvg waiting time : {:.2f}".format(sum_wt))
    #print("Avg turnaround time : {:.2f}".format(sum_tr))
    #print("Throughput : {:.2f} process/sec\n".format(totalprocess / (s_time[-1])))


# Calculate queue non-preem-prioriy
find_va()

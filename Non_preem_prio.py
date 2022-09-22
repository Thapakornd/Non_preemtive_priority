''' 
1. Sort the arrival time
2. if arrival time same focus priority
3. apply FCFS
'''

arrivaltime = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
bursttime = [10, 20, 5, 3, 15, 25, 10, 25, 5, 10, 2, 20, 10, 20, 5, 3, 15, 25, 10, 25]
priority = [3, 2, 1, 5, 4, 2, 1, 1, 3, 3, 5, 5, 3, 2, 1, 5, 4, 2, 1, 1]
totalprocess = len(arrivaltime)
proc = []

for i in range(totalprocess):
    # init value to calculate
    # P_num , Burst_t, Arr_t, Priority
    l = []
    for j in range(4):
        l.append(0)
    proc.append(l)

# Sort arrival time each process
def sort_proc():
    temp = []
    for j in range(totalprocess):
        for i in range(0,totalprocess-j-1,1):
            if proc[i][0] > proc[i+1][0]: # swap value p[i] and p[i+1]
                temp = proc[i]
                proc[i] = proc[i+1]
                proc[i+1] = temp

# Sort Priority each arrival time
def sort_prio(b_t,p_t):
    # Check value while arrival time 
    stk = 0
    for i in range(p_t,totalprocess):
        if proc[i][0] < b_t:
            stk += 1
    
    for i in range(stk): # <---- swap Process with priority
        for j in range(p_t,stk-i,+1):
            if proc[j][2] > proc[j+1][2]:
                temp = proc[j]
                proc[j] = proc[j+1]
                proc[j+1] = temp

def find_va():
    s_time = [0] * (totalprocess+1)  # <------ Comput time each process
    tr_t = [0] * totalprocess   # <------ Turn around time each process
    wt = [0] * totalprocess   # <------ Waiting time each process
    cpu_util = []
    thr_p = []
    s_time[0] = 0  # <------ Set P1 start 0 
    p_t = 0  # <---- Set Process computed
    sum_wt = 0
    sum_tr = 0
    
    # Function sort arrival time    
    sort_proc()

    for i in range(totalprocess):
        # Function create value each process
        s_time[i+1] = proc[i][1] + s_time[i]
        tr_t[i] = s_time[i+1] - proc[i][0]
        wt[i] = tr_t[i] - proc[i][1]
        p_t =+ 1
        sum_wt = sum_wt + wt[i] 
        sum_tr = sum_tr + tr_t[i]                  
        sort_prio(s_time[i+1],p_t)   # <---- Get value to sort prioriy

        # Avg of waiting time and turn around time
        sum_wt = sum_wt / totalprocess
        sum_tr = sum_tr / totalprocess

    # Output
    print("\nProcess \tArrivaltime \tBursttime \tPriority \tWaiting \tTurnaround")
    for i in range(totalprocess):
        print("P{} \t\t{} \t\t{} \t\t{} \t\t{} \t\t{}".format(proc[i][3],proc[i][0],proc[i][1],proc[i][2],wt[i],tr_t[i]))
    print("\nAvg waiting time : {:.2f}".format(sum_wt))
    print("Avg turnaround time : {:.2f}\n".format(sum_tr))
        
'''
    proc 0 : arrival time
    proc 1 : burst time
    proc 2 : priority
    proc 3 : process number
'''
# init value to each process
for i in range(totalprocess):
    proc[i][0] = arrivaltime[i]
    proc[i][1] = bursttime[i]
    proc[i][2] = priority[i]
    proc[i][3] = i + 1

# Use func to calculate
find_va()



        
    
        
        
        

''' 
1. Sort the arrival time
2. if arrival time same focus priority
3. apply FCFS
'''

arrivaltime = [0, 5, 12, 2, 9]
bursttime = [11, 28, 2, 10, 16]
priority = [2, 0, 3, 1, 4]
totalprocess = len(arrivaltime)
proc = []
for i in range(totalprocess):
    # init value to calculate
    # P_num , Burst_t, Arr_t, Priority
    l = []
    for j in range(4):
        l.append(0)
    proc.append(l)

# Find max arrival time 
max_arr = 0
for i in range(totalprocess):
    if arrivaltime[i] > max_arr:
        max_arr = arrivaltime[i]

def sort_proc():
    temp = []
    # Sort arrival time each process
    for j in range(totalprocess):
        for i in range(0,totalprocess-j-1,1):
            if proc[i][0] > proc[i+1][0]:
                temp = proc[i]
                proc[i] = proc[i+1]
                proc[i+1] = temp

    # Sort priorty each Process
    '''for j in range(totalprocess):
        for i in range(1,totalprocess-j-1,1):
            if proc[i][2] < proc[i+1][2]:
                temp = proc[i]
                proc[i] = proc[i+1]
                proc[i+1] = temp
    '''    
def sort_prio(b_t,a_t): #<--- Burst time arrival
    # Sort Priority each arrival time
    stk = 0
    for i in range(a_t,totalprocess):
        if proc[i][0] < b_t:
            stk += 1
    
    for i in range(stk):
        for j in range(a_t,stk-i,+1):
            if proc[j][2] > proc[j+1][2]:
                temp = proc[j]
                proc[j] = proc[j+1]
                proc[j+1] = temp

def find_va():
    s_time = [0] * (totalprocess+1)
    tr_t = [0] * totalprocess
    wt = [0] * totalprocess
    s_time[0] = 0
    b_t = 0
    a_t = 0
    
    sort_proc()
    # Sort computtime
    for i in range(totalprocess):
        # Function Sort Prio in here
        s_time[i+1] = proc[i][1] + s_time[i]
        tr_t[i] = s_time[i+1] - proc[i][0]
        wt[i] = tr_t[i] - proc[i][1]
        b_t = s_time[i+1]
        a_t =+ 1
        sort_prio(b_t,a_t)
    

'''
    proc 0 : arrival time
    proc 1 : burst time
    proc 2 : priority
    proc 3 : process number
'''
for i in range(totalprocess):
    proc[i][0] = arrivaltime[i]
    proc[i][1] = bursttime[i]
    proc[i][2] = priority[i]
    proc[i][3] = i + 1

find_va()
for i in range(totalprocess):
    print("\tP"+ str(proc[i][3]) + " : " + str(proc[i]))
#print(find_va())


        
    
        
        
        

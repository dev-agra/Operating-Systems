# 4
# ID AS INTEGER
from prettytable import PrettyTable


def findWaitingTime(processes, n, wt):
    rt = [0] * n

    # Copy the burst time into rt[]
    for i in range(n):
        rt[i] = processes[i][1]
    complete = 0
    t = 0
    minm = 999999999
    short = 0
    check = False

    # Process until all processes gets
    # completed
    while complete != n:

        # Find process with minimum remaining
        # time among the processes that
        # arrives till the current time`
        for j in range(n):
            if ((processes[j][2] <= t) and
                    (rt[j] < minm) and rt[j] > 0):
                minm = rt[j]
                short = j
                check = True
        if not check:
            t += 1
            continue

        # Reduce remaining time by one
        rt[short] -= 1

        # Update minimum
        minm = rt[short]
        if minm == 0:
            minm = 999999999

        # If a process gets completely
        # executed
        if rt[short] == 0:

            # Increment complete
            complete += 1
            check = False

            # Find finish time of current
            # process
            fint = t + 1

            # Calculate waiting time
            wt[short] = (fint - processes[short][1] -
                         processes[short][2])

            if wt[short] < 0:
                wt[short] = 0

        # Increment time
        t += 1


# Function to calculate turn around time
def findTurnAroundTime(process, n1, wait, tat):
    # Calculating turnaround time
    for j in range(n1):
        tat[j] = process[j][1] + wait[j]


def findavg_time(process, num, p, arrival, burst):
    x = PrettyTable()
    wait_tym = [0] * num
    turnard_tym = [0] * num

    column_names = ["Process", "Burst Time", "Arrival Time", "Waiting Time", "Turnaround Time"]

    findWaitingTime(process, num, wait_tym)
    findTurnAroundTime(process, num, wait_tym, turnard_tym)

    total_waittym = 0
    total_turnardtym = 0

    for i in range(num):
        total_waittym += wait_tym[i]
        total_turnardtym += turnard_tym[i]

    x.add_column(column_names[0], p)
    x.add_column(column_names[1], arrival)
    x.add_column(column_names[2], burst)
    x.add_column(column_names[3], wait_tym)
    x.add_column(column_names[4], turnard_tym)

    print(x)

    print(f"Average waiting time = {total_waittym/num}")
    print(f"Average Turnaround time = {total_turnardtym/num}")


def creation():
    num_process = int(input("How many Processes would you like to have?: "))
    process = []
    arrival_tym = []
    burst_tym = []
    p = [0] * num_process

    for i in range(0, num_process):  # Inputting process Parameters
        attributes = []
        print("")
        print(f"For process {i + 1}")
        id1 = int(input("Enter the process id: "))
        attributes.append(id1)
        burst = int(input("Enter the burst time of the process: "))
        attributes.append(burst)
        arrival = int(input("Enter the arrival time of the process: "))
        attributes.append(arrival)       # Small list with individual process attributes

        process.append(attributes)  # Full list with attributes of n processes

    # Creating separate list of arrival | burst time
    for i in range(0, num_process):
        arrival_tym.append(process[i][1])
        burst_tym.append(process[i][2])

    # Printing arrival and burst times
    print(f"Arrival time of processes are: {arrival_tym}")
    print(f"Burst time of processes are: {burst_tym}")

    for i in range(0, len(process)):  # Process Name for the Table
        p[i] = process[i][0]

    findavg_time(process, num_process, p, arrival_tym, burst_tym)


creation()

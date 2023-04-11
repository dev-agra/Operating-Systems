# 4
from prettytable import PrettyTable


def arrange_arrival(n, array):
    for i in range(0, n):
        for j in range(i, n-i-1):
            if array[1][j] > array[1][j+1]:
                for k in range(0, n):
                    array[k][j], array[k][j+1] = array[k][j+1], array[k][j]


def CompletionTime(n, array):
    value = 0
    array[3][0] = array[1][0] + array[2][0]
    array[5][0] = array[3][0] - array[1][0]
    array[4][0] = array[5][0] - array[2][0]
    for i in range(1, n):
        temp = array[3][i-1]
        mini = array[2][i]
        for j in range(i, n):
            if temp >= array[1][j] and mini >= array[2][j]:
                mini = array[2][j]
                value = j
        array[3][value] = temp + array[2][value]
        array[5][value] = array[3][value] - array[1][value]
        array[4][value] = array[5][value] - array[2][value]
        for k in range(0, 6):
            array[k][value], array[k][i] = array[k][i], array[k][value]


def creation():
    x = PrettyTable()
    column_names = ["Process", "Arrival Time", "Burst Time", "Completion Time", "Waiting Time", "Turnaround Time"]

    num_process = int(input("How many Processes would you like to have?: "))
    process = []
    arrival_tym = []
    burst_tym = []
    comp_tym = [0] * num_process
    wait_tym = [0] * num_process
    turnard_tym = [0] * num_process
    p = [0] * num_process

    for i in range(0, num_process):  # Inputting process Parameters
        attributes = []
        print("")
        print(f"For process {i + 1}")
        id1 = input("Enter the process id: ")
        attributes.append(id1)
        arrival = int(input("Enter the arrival time of the process: "))
        attributes.append(arrival)
        burst = int(input("Enter the burst time of the process: "))
        attributes.append(burst)  # Small list with individual process attributes

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

    arr = [p, arrival_tym, burst_tym, comp_tym, wait_tym, turnard_tym]
    arrange_arrival(num_process, arr)
    CompletionTime(num_process, arr)

    x.add_column(column_names[0], arr[0])
    x.add_column(column_names[1], arr[1])
    x.add_column(column_names[2], arr[2])
    x.add_column(column_names[3], arr[3])
    x.add_column(column_names[4], arr[4])  # Wait
    x.add_column(column_names[5], arr[5])  # Turnaround
    print(x)

    total_waittym = 0
    total_turnarndtym = 0
    for i in range(0, num_process):
        total_waittym += arr[4][i]
        total_turnarndtym += arr[5][i]

    print(f"Average waiting time = {total_waittym / num_process}")
    print(f"Average Turnaround time = {total_turnarndtym / num_process}")


creation()

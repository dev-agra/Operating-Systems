# Arrival same
from prettytable import PrettyTable


def creation():
    x = PrettyTable()
    column_names = ["Process", "Arrival Time", "Burst Time", "Waiting Time", "Turnaround Time", "Completion Time"]

    num_process = int(input("How many Processes would you like to have?: "))
    process = []
    arrival_tym = []
    burst_tym = []
    wait_tym = [0] * num_process
    turnaround = [0] * num_process
    p = [0] * num_process

    for i in range(0, num_process):
        attributes = []
        print("")
        print(f"For process {i + 1}")
        id1 = input("Enter the process id: ")
        attributes.append(id1)
        arrival = int(input("Enter the arrival time of the process: "))
        attributes.append(arrival)
        burst = int(input("Enter the burst time of the process: "))
        attributes.append(burst)

        process.append(attributes)

    for i in range(0, num_process):
        arrival_tym.append(process[i][1])
        burst_tym.append(process[i][2])

    print(f"Arrival time of processes are: {arrival_tym}")
    print(f"Burst time of processes are: {burst_tym}")

    for i in range(1, len(burst_tym)):
        wait_tym[i] = wait_tym[i - 1] + burst_tym[i - 1]
    print(wait_tym)

    for i in range(0, len(burst_tym)):
        turnaround[i] = wait_tym[i] + burst_tym[i]
    print(turnaround)

    for i in range(0, len(process)):
        p[i] = process[i][0]

    x.add_column(column_names[0], p)
    x.add_column(column_names[1], arrival_tym)
    x.add_column(column_names[2], burst_tym)
    x.add_column(column_names[3], wait_tym)
    x.add_column(column_names[4], turnaround)
    print(x)


creation()

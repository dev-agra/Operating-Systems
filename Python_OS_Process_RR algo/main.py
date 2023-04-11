# Enter process id as an integer

from prettytable import PrettyTable


def schedulingProcess(process_data, time_slice):
    start_time = []
    exit_time = []
    executed_process = []
    ready_queue = []
    runtime = 0
    process_data.sort(key=lambda x: x[1])

    # Sort processes according to the Arrival Time
    while 1:
        normal_queue = []
        temp = []
        for i in range(len(process_data)):

            # Checks if arrival = runtime and not completed ie. Flag  = 0
            if process_data[i][1] <= runtime and process_data[i][3] == 0:
                present = 0
                # Checks that the next process is not a part of ready_queue
                if len(ready_queue) != 0:
                    for k in range(len(ready_queue)):
                        if process_data[i][0] == ready_queue[k][0]:
                            present = 1

                # Adds a process to the ready_queue only if it is not already present in it
                if present == 0:
                    temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                    ready_queue.append(temp)
                    temp = []

                # Makes sure that the recently executed process is appended at the end of ready_queue
                if len(ready_queue) != 0 and len(executed_process) != 0:
                    for k in range(len(ready_queue)):
                        if ready_queue[k][0] == executed_process[len(executed_process) - 1]:
                            ready_queue.insert((len(ready_queue) - 1), ready_queue.pop(k))

            elif process_data[i][3] == 0:
                temp.extend([process_data[i][0], process_data[i][1], process_data[i][2], process_data[i][4]])
                normal_queue.append(temp)
                temp = []

        if len(ready_queue) == 0 and len(normal_queue) == 0:
            break

        # If process has remaining burst time greater than the quantum time, it will execute for a time period equal
        #                  to quantum time and then switch
        if len(ready_queue) != 0:
            if ready_queue[0][2] > time_slice:
                start_time.append(runtime)
                runtime = runtime + time_slice
                e_time = runtime
                exit_time.append(e_time)
                executed_process.append(ready_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == ready_queue[0][0]:
                        break
                process_data[j][2] = process_data[j][2] - time_slice
                ready_queue.pop(0)

            # If a process has a remaining burst time less than or equal to quantum time, it will complete its execution
            elif ready_queue[0][2] <= time_slice:
                start_time.append(runtime)
                runtime = runtime + ready_queue[0][2]
                e_time = runtime
                exit_time.append(e_time)
                executed_process.append(ready_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == ready_queue[0][0]:
                        break
                process_data[j][2] = 0
                process_data[j][3] = 1
                process_data[j].append(e_time)
                ready_queue.pop(0)

        elif len(ready_queue) == 0:
            if runtime < normal_queue[0][1]:
                runtime = normal_queue[0][1]

            # If process has remaining burst time greater than the quantum time, it will execute for a time period equal
            #                  to quantum time and then switch
            if normal_queue[0][2] > time_slice:
                start_time.append(runtime)
                runtime = runtime + time_slice
                e_time = runtime
                exit_time.append(e_time)
                executed_process.append(normal_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == normal_queue[0][0]:
                        break
                process_data[j][2] = process_data[j][2] - time_slice

            # If a process has a remaining burst time less than or equal to quantum time, it will complete its execution
            elif normal_queue[0][2] <= time_slice:
                start_time.append(runtime)
                runtime = runtime + normal_queue[0][2]
                e_time = runtime
                exit_time.append(e_time)
                executed_process.append(normal_queue[0][0])
                for j in range(len(process_data)):
                    if process_data[j][0] == normal_queue[0][0]:
                        break
                process_data[j][2] = 0
                process_data[j][3] = 1
                process_data[j].append(e_time)

    # Calling appropriate Methods
    t_time = calculateTurnaroundTime(process_data)
    w_time = calculateWaitingTime(process_data)
    table_creation(process_data, t_time, w_time, executed_process)


def calculateTurnaroundTime(process_data):
    total_turnaround_time = 0
    for i in range(len(process_data)):
        turnaround_time = process_data[i][5] - process_data[i][1]
        '''
        turnaround_time = completion_time - arrival_time
        '''
        total_turnaround_time = total_turnaround_time + turnaround_time
        process_data[i].append(turnaround_time)
    average_turnaround_time = total_turnaround_time / len(process_data)
    '''
    average_turnaround_time = total_turnaround_time / no_of_processes
    '''
    return average_turnaround_time


def calculateWaitingTime(process_data):
    total_waiting_time = 0
    for i in range(len(process_data)):
        waiting_time = process_data[i][6] - process_data[i][4]
        '''
        waiting_time = turnaround_time - burst_time
        '''
        total_waiting_time = total_waiting_time + waiting_time
        process_data[i].append(waiting_time)
    average_waiting_time = total_waiting_time / len(process_data)
    '''
    average_waiting_time = total_waiting_time / no_of_processes
    '''
    return average_waiting_time


def table_creation(process, avg_turn, avg_wait, executed_process):
    # process.sort(lambda x: x[0])
    x = PrettyTable()

    x.field_names = ["Process", "Arrival Time", "Rem_Burst_Time", "Completed", "Burst_Time", "Completion Time",
                     "Turnaround Time", "Waiting Time"]
    for i in range(len(process)):
        x.add_row(process[i])
    print("")
    print(x)
    print(f"Average Turnaround Time is: {avg_turn}")
    print(f"Average Waiting Time is: {avg_wait}")
    print(f"Sequence of execution is: {executed_process}")


def creation():
    num_process = int(input("How many Processes would you like to have?: "))
    quan_tym = int(input("Enter the time quantum: "))
    process = []
    arrival_tym = []
    burst_tym = []

    for i in range(num_process):
        attributes = []
        print("")
        print(f"For process {i + 1}")
        id1 = int(input("Enter the process id: "))
        attributes.append(id1)
        arrival = int(input("Enter the arrival time of the process: "))
        attributes.append(arrival)
        burst = int(input("Enter the burst time of the process: "))
        attributes.append(burst)  # Attributes of single process - individual list process
        attributes.append(0)
        attributes.append(burst)
        process.append(attributes)  # Major List has n list processes

    for i in range(0, num_process):
        arrival_tym.append(process[i][1])
        burst_tym.append(process[i][2])

    print(f"Arrival time of processes are: {arrival_tym}")
    print(f"Burst time of processes are: {burst_tym}")

    schedulingProcess(process, quan_tym)


creation()

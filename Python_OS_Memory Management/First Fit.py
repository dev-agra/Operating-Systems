num_process = int(input("Enter the number of Processes: "))

processes = [int(x) for x in input("Enter the sizes of process blocks: ").split(' ')]
memory = [int(x) for x in input("Enter the sizes of memory blocks: ").split(' ')]


allocation = [0] * len(processes)

for i in range(len(processes)):
    for j in range(len(memory)):
        if memory[j] >= processes[i]:
            allocation[i] = 1
            memory[j] -= processes[i]
            break

for i in range(len(allocation)):
    if allocation[i] == 1:
        pass
    elif allocation[i] == 0:
        print(f"Process {i+1} is not allocated i.e. -> {processes[i]}")






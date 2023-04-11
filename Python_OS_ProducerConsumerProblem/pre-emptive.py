class ProblemConsumer:
    Buff_size = int(input("Enter the size of the buffer: "))
    Buffer = [0] * Buff_size
    In = 0
    Out = 0
    S = 1
    Empty = Buff_size
    Full = 0

    @classmethod
    def Producer(cls):
        flag = True
        while flag:
            if cls.S == 0:
                print("Process in Critical Section in other process")
                break
            if cls.Empty == 0 or cls.Full == cls.Buff_size:
                print("Buffer is full!\n")
                flag = False
            elif cls.Empty <= cls.Buff_size and cls.Full >= 0:
                itemp = int(input("Enter the item to be added to the buffer: "))
                cls.Empty -= 1
                cls.S -= 1                                      # If S==0 then process in Critical Section
                print('CONTEXT SWITCH')
                ProblemConsumer.Consumer()  # Context Switch
                cls.Buffer[cls.In] = itemp
                cls.In = (cls.In + 1) % cls.Buff_size
                cls.S += 1
                cls.Full += 1
                print(f'Buffer-> {ProblemConsumer.Buffer}\nEmpty->{ProblemConsumer.Empty}\nIn->{ProblemConsumer.In}\nOut->{ProblemConsumer.Out}\nFull->{ProblemConsumer.Full}\nS->{ProblemConsumer.S}')
                print("Producer Process Completed!\n")
                ProblemConsumer.Consumer()

    @classmethod
    def Consumer(cls):
        flag = True
        while flag:
            if cls.S == 0:
                print("Process in Critical Section in other process")
                break
            if cls.Empty == cls.Buff_size or cls.Full == 0:
                print("Buffer is empty!\n")
                flag = False
            elif cls.Empty < cls.Buff_size and cls.Full > 0:
                cls.Full -= 1
                cls.S -= 1
                print('CONTEXT SWITCH')
                ProblemConsumer.Producer()
                itemc = cls.Buffer.pop(cls.Out)
                print(f'Item removed by the Consumer is: {itemc}')
                cls.Buffer.insert(cls.Out, 0)
                cls.Out = (cls.Out + 1) % cls.Buff_size
                cls.S += 1
                cls.Empty += 1
                flag = False
                print(f'Buffer-> {ProblemConsumer.Buffer}\nEmpty->{ProblemConsumer.Empty}\nIn->{ProblemConsumer.In}\nOut->{ProblemConsumer.Out}\nFull->{ProblemConsumer.Full}\nS->{ProblemConsumer.S}')
                print("Consumer Process Completed!\n")
                ProblemConsumer.Producer()


problem = ProblemConsumer()
problem.Producer()
print(ProblemConsumer.Buffer)

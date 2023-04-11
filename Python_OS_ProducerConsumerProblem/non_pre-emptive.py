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
            if cls.Empty == 0 or cls.Full == cls.Buff_size:
                print("Buffer is full!\n")
                # flag = False
                break
            itemp = int(input("Enter the item to be added to the buffer: "))
            cls.Empty -= 1
            cls.S -= 1
            cls.Buffer[cls.In] = itemp
            cls.In = (cls.In + 1) % cls.Buff_size
            cls.S += 1
            cls.Full += 1
            # print(f'{Buff_size} {empty} {full}')
            print("Producer Process Completed!\n")

    @classmethod
    def Consumer(cls):
        flag = True
        while flag:
            if cls.Empty == cls.Buff_size or cls.Full == 0:
                print("Buffer is empty!\n")
                # flag = False
                break
            cls.Full -= 1
            cls.S -= 1
            itemc = cls.Buffer.pop(cls.Out)
            print(f'Item removed by the Consumer is: {itemc}')
            cls.Buffer.insert(cls.Out, 0)
            cls.Out = (cls.Out + 1) % cls.Buff_size
            cls.S += 1
            cls.Empty += 1
            print("Consumer Process Completed!\n")


problem = ProblemConsumer()
problem.Producer()
problem.Producer()
problem.Consumer()
problem.Consumer()
problem.Consumer()
print(ProblemConsumer.Buffer)
print(f'{ProblemConsumer.Empty} {ProblemConsumer.In} {ProblemConsumer.Out} {ProblemConsumer.Full} {ProblemConsumer.S}')

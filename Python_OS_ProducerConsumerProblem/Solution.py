# If first Producer is called and Consumer tries to enter do make sure that Consumer has a If condition
# stating cls.S == 0 then Another in CS likes
#
from colorama import Fore


def wait(mutex):
    if mutex <= 0:
        pass
    else:
        mutex -= 1
    return mutex


def signal(mutex):
    mutex += 1
    return mutex


class ProblemConsumer:
    Buff_size = int(input("Enter the size of the buffer: "))
    Buffer = [] * Buff_size
    S = 1
    Empty = Buff_size
    Full = 0

    @classmethod
    def Producer(cls):
        if cls.S == 0:
            print(Fore.RED + "Another process in CS" + Fore.RESET)
        elif cls.Empty == 0 or cls.Full == cls.Buff_size:
            print("Buffer is full!\n")
            # flag = False
        else:
            flag = True
            while flag:
                # If S==1 not in CS, if S==0 in CS
                cls.Empty = wait(cls.Empty)
                # Acquiring a lock as in a mutex one
                cls.S = wait(cls.S)

                print("--------------------------------------")
                print("-----Producer in Critical Section-----\n")
                item = int(input("Enter the item to add: "))
                print("Adding data to buffer..")
                cls.Buffer.append(item)

                # ProblemConsumer.Consumer()

                # Releasing the lock
                cls.S = signal(cls.S)
                # Increment Full as Producer Adds Item
                cls.Full = signal(cls.Full)
                flag = False

    @classmethod
    def Consumer(cls):
        if cls.S == 0:
            print(Fore.RED + "Another process in CS" + Fore.RESET)
        elif cls.Empty == cls.Buff_size or cls.Full == 0:
            print("Buffer is empty!\n")
            # flag = False
        else:
            flag = True
            while flag:
                # If S==1 not in CS, if S==0 in CS
                cls.Full = wait(cls.Full)
                # Acquiring a lock as in a mutex one
                cls.S = wait(cls.S)

                print("--------------------------------------")
                print("-----Consumer in Critical Section-----\n")
                print("Removing data from buffer..")
                cls.Buffer.pop()

                ProblemConsumer.Producer()

                # Releasing the lock
                cls.S = signal(cls.S)
                # Increment Empty as Consumer removes Item
                cls.Empty = signal(cls.Empty)
                flag = False


problem = ProblemConsumer()
problem.Producer()
problem.Producer()
problem.Consumer()
print(f'{problem.Buffer} {problem.Empty} {problem.Full} {problem.S}')

import os


def parent_child():
    n = os.fork()
    if n > 0:
        print(f"Parent process and is is:{os.getpid()}")
    else:
        print(f"Child process and is is: {os.getpid()}")


parent_child()


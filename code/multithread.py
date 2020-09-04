#importing os package
import os
#importing threading package for multithreading
import threading


def new_child():
    n = os.fork()
    
    if n == 0:
        print("pid of child process is {}".format(os.getpid()))
    else:
        print("parent id")

new_child()


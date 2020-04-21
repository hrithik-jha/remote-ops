import threading
import components.mid as task1
from multiprocessing import Process

def schedule(id=-1):
    # Task 1
    # Task 2 task1.task() // for non-thread workflow
    if id != -1:
        thread = Process(target=task1.task, args=(id))
        # Other thread/id related tasks
    else:
        thread = Process(target=task1.task, args=())
    print("Starting thread")
    thread.start()
    
    # if a value has to be returned, do not use threads.
    # initiate a return chain of values to the main.py
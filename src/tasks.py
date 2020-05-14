import threading
import components.mid as task1
from multiprocessing import Process

'''
The second variable in the Tuple suggest if the function is thread-safe or not
tasks = [
    (task1(), False)
    (task2(), True)
    (task3(), False)
]
'''

'''
GUIDE TO CHOOSING BETWEEN THREADS AND FUNCTION CALLS:
- IF YOU NEED TO FOLLOW A CERTAIN ORDER OF TASKS: FUNCTION CALL
- IF NO ORDER IS NECESSARY, ALL TASKS NEED TO BE COMPLETED: THREAD FUNCTION CALL
'''

def schedule(id=-1):
    callStack = []
    for task in tasks:
        if task[1]:
            thread = Process(target=task[0], args=(id))
            thread.start()
        else:
            callStack.append(task[0])
    results = [f() for f in callStack]
    # if a value has to be returned, do not use threads.
    # initiate a return chain of values to the main.py
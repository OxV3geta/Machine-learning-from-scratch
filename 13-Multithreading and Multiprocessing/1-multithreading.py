### Multithreding
## When to use Multi Threding-
### I/O-bound task : Task that spend more time waiting for I/O operations (e.g. file operations, network operations.
### Concurrent execution : When we want to improve throughput of our application by performing multiple concurrently.

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Numbers:{i}")

'''this program is not running until the first function completed it's execution because the first 
function wirtten first and they are in the single thred.
'''
def print_letter():
    for i in 'abcd':
        # time.sleep(3)
        print(i)
        
## create 2 threads
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)
'''
by creating 2 thread, so when we run the program the 2nd thread run the 2nd function immediately and wait for the 
1st function to complete execution. even if we give both of them the sleep(suspends) then the both run equally and the execution time decreased 
by half compare then the single thread.'''

start_time = time.time()
## start the thread
t1.start()
t2.start()

### wait for the other thread complete
t1.join()
t2.join() 
finished_time = time.time() - start_time
print(finished_time)


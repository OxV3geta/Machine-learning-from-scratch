## Processes that run in parallel
# When we use multi processing-
### CPU-Bond Tasks - Tasks That are heavy on CPU usage(e.g., mathematical computations, data processing).
### Parallel execution -  Multiple Cores of the CPU

import multiprocessing
import time

def squre_numbers():
    for i in range(5):
        time.sleep(1)
        print(f"Squre:{i*i}")

def cube_numbers():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube:{i*i*i}")

## creating 2 processes
p1 = multiprocessing.Process(target=squre_numbers)
p2 = multiprocessing.Process(target=cube_numbers)

start_time = time.time()

## start the process
p1.start()
p2.start()

## wait fof the process to complete

p1.join()
p2.join()

finished_time = time.time() - start_time


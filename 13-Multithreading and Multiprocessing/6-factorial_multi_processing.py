'''
Real world Example:: Multiprocessing for I/O-bounds Tasks
Scenario : Factorial Calculation
Factorial calculations,espeacilly for large number,
involve significant computational work .
Multiprocessing can be used to distribute the workload across multiple CPU cores,
improving performance.
'''
import multiprocessing
import math
import sys
import time

# Increase the maximum number of digits for integer conversion
sys.set_int_max_str_digits(100000)

## function to complete factorials of given number

def computer_factorial(number):
    print(f'computing factorial of number')
    result = math.factorial(number)
    print(f'Factorial of {number} is {result}')
    return result

if __name__ == '__main__':
    numbers = [5000,6000,7000,8000]
    
    start_time = time.time()
    
    ## create a pool of worker process
    
    with multiprocessing.Pool(processes=1) as pool:
        results = pool.map(computer_factorial,numbers)
    
    
    time_taken = time.time() - start_time
    
    print(f'Result:{results}')
    print(f'Time taken:{time_taken} Seconds')
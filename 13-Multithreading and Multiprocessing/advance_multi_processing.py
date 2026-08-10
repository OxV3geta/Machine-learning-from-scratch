### Multiprocessing with Process Pool Executor

from concurrent.futures import ProcessPoolExecutor
import time

def squre_number(number):
    time.sleep(1)
    return f"Squre: {number*number}"

numbers = [1,2,3,4,5,6,7,8,9,11,10,2,14,12]

if __name__ == '__main__':
    ## execute the code using 3 process
    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(squre_number,numbers)
        
    for result in results:
        print(result)


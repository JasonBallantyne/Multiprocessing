import time
import math
import multiprocessing

# function to return the square
def my_func(x):
    s = math.sqrt(x)
    return s

# This verbose version shows which process in the pool is running each task
def my_func_verbose(x):
    s = math.sqrt(x)
    print("Task", multiprocessing.current_process(), x, s)
    return s

# A naive function for checking primes
def check_prime(num):
    t1 = time.time()
    res = False
    list1 = []
    if num > 0:
        # check for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                print("Time:", int(time.time()-t1))
                break
        else:
            print(num,"is a prime number")
            time1 = time.time()-t1
            print("Time:", time1)
            list1.append(time1)
            res = True
            # if input number is less than
            # or equal to 1, it is not prime
    return res

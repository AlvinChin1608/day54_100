"""
Objective
Create your own decorator function to measure the amount of seconds that a function takes to execute.

Expected Output
1695050908.1985211
fast_function run speed: 0.33974480628967285s
slow_function run speed: 2.9590742588043213

"""

import time
current_time = time.time()
print(current_time) # seconds since Jan 1st, 1970

# Write your code below 👇

def speed_calc_decorator(function):
    def wrapper_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time-start_time}s")
    return wrapper_function

@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i

fast_function()
slow_function()

# Output:
# 1721213261.574354
# fast_function run speed: 0.07558703422546387s
# slow_function run speed: 0.6154699325561523s
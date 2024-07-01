"""
Created on Fri Mar 19 15:20:56 2021

@author: Dhin Islam Md

Generating all prime number from given input and find out if the input number "Prime or not"
Version 1.0

Inputs [997, 1000, 5000, 6879, 8999]
"""

import time   # For Time Function

def prime_num_1(num): 
    """This fucntion will return 'True' if 'num' is a prime number. 
    Otherwise return 'False'"""
    
    if num == 1:
        return False # Number 1 is not prime number
    
    for f in range(2, num): 
        """Loop all number from 2 through num minus 1"""
        if num % f == 0: 
            """This will give the reminder when num devided by f and if the 
            reminder is 0, then num has a divisor other itself and 1, So num is not prime"""
            return False
    return True # Otherwise True

n = 100 # Input
list_primes = [] #This will list the prime numbers

# Time Function
start = time.time()

# List Function to list prime numbers
for num in range(1,n+1):
    """This will run all numbers from 1 through all the way up to input size"""
    
    counter = 0
    for f in range (1, num+1):
        if num % f == 0:
            counter = counter + 1
    if counter == 2:
        list_primes.append(num)
        prime_num_1(num)
        
print(list_primes, n , prime_num_1(num))

end = time.time()  # End time function
print( "Time = {}".format(end-start))

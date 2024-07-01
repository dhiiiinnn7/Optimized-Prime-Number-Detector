"""
Created on Fri Mar 19 18:30:50 2021

@author: Dhin Islam Md

Generating all prime number from given input and find out if the input number "Prime or not"
Version 2.0
For this 2nd version, I will test divisors from 2 through sqrt(num) then test 
if 'num is even' and test only odd divisors

Inputs [997, 1000, 5000, 6879, 8999]
"""

import math       # To use the Square roots, you need to import the mathe module
import time       # For time function

def prime_num_2(num): 
    """This fucntion will return 'True' if 'num' is a prime number. 
    Otherwise return 'False'"""
    if num == 1:
        return False # Because number 1 is not prime number
    if num == 2:
        return True  # Becuase 2 is the only even prime number
    if num > 2 and num % 2 == 0:
        return False  # O and 1 are not prime numbers
    
    max_divisor = math.floor(math.sqrt(num))
    """finding the largest possible divisor = take the square root 'num' 
    then round down using the floor function"""
    for f in range(3, 1 + max_divisor, 2): 
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
for num in range(2, n + 1):
    """This will run all numbers from 2 through all the way up to input size"""
    
    counter = 0
    for f in range (2, int(num ** 0.5) + 1):
        """ Range starts with 2 and only needs to go up and the square root of 'num' for 
        all odd numbers"""
        if num % f == 0:
            counter = counter + 1
    if counter == 2:
        list_primes.append(num)
        prime_num_2(num)
        
print(list_primes, n , prime_num_2(num))

end = time.time()  # End time function
print( "time = {}".format(end-start))

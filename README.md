# Efficient Prime Number Generation in Python

## Overview

A system that identifies prime numbers within a given range using two distinct and efficient algorithms.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Algorithm Description](#algorithm-description)
  - [Solution 1](#solution-1)
  - [Solution 2](#solution-2)
- [Running the Code](#running-the-code)
- [Performance Analysis](#performance-analysis)
- [License](#license)

## Project Structure

- `prime_number_1.py`: First version of the prime number generation and checking script.
- `prime_number_2.py`: Second version of the prime number generation and checking script (Second version is faster).

## Installation

### Clone the Repository
```sh
git clone https://github.com/dhiiiinnn7/Optimized-Prime-Number-Detector.git
```

### Navigate to the Project Directory
```sh
cd Optimized-Prime-Number-Detector
```

## Algorithm Description

### Solution 1

This version generates all prime numbers up to a given input `n` and checks if a specific number is prime by looping through all numbers from 2 to `n-1`.

```python
def prime_num_1(num): 
    if num == 1:
        return False
    for f in range(2, num):
        if num % f == 0:
            return False
    return True
```

- Time Complexity: O(N^2)
- Space Complexity: O(N)

### Solution 2

This version improves efficiency by testing divisors from 2 through √n and only tests odd divisors after checking if the number is even.

```python
import math

def prime_num_2(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num > 2 and num % 2 == 0:
        return False

    max_divisor = math.floor(math.sqrt(num))
    for f in range(3, 1 + max_divisor, 2):
        if num % f == 0:
            return False
    return True
```

- Time Complexity: O(n√n)
- Space Complexity: O(n)

### Run the Python script

- Solution 1
  
```sh
python prime_number_1.py
```

- Solution 2

```sh
python prime_number_2.py
```

## Performance Analysis

The second solution is more efficient, as shown in the performance analysis section of the report. Here is a comparison of the time taken for different input sizes:

- Inputs: [997, 1000, 5000, 6879, 8999]
- Solution 2 is approximately twice as fast as Solution 1.

Graphs and detailed analysis are available in the provided report.

## License
This project is licensed under the Apache License 2.0 - see the LICENSE file for details.

# -*- coding: utf-8 -*-
"""ProjEulerProb12

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Td2AWFHNyQ43JSCpJ7MX2FumR6fKPcU8
"""

import time

# returns the nth triangle number; that is, the sum of all the natural numbers less than, or equal to, n
def triangleNumber(n):
    return sum ( [ i for i in range(1, n + 1) ] )

start = int(round(time.time() * 1000)) # starts the stopwatch

j = 0 # j represents the jth triangle number
n = 0 # n represents the triangle number corresponding to j
numberOfDivisors = 0 # number of divisors for triangle number n

while numberOfDivisors <= 500:

    # resets numberOfDivisors because it's now checking a new triangle number
    # and also sets n to be the next triangle number
    numberOfDivisors = 0
    j += 1
    n = triangleNumber(j)

    # for every number from 1 to the square root of this triangle number,
    # count the number of divisors
    i = 1
    while i <= n**0.5:
        if n % i == 0:
            numberOfDivisors += 1
        i += 1

    # 1 to the square root of the number holds exactly half of the divisors
    # so multiply it by 2 to include the other corresponding half
    numberOfDivisors *= 2

finish = int(round(time.time() * 1000)) # stops the stopwatch

print (n)
print ("Time taken: " + str(finish-start) + " milliseconds")
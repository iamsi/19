#imports
import time
import sympy
import primesieve

it = primesieve.Iterator()
StartTime = time.time()
CurrPrime = it.next_prime()
n = 1
total = 0

while True:
    total = total + (CurrPrime ** 2)
    CurrPrime = CurrPrime = it.next_prime()
    if ( total % n == 0):
        print ("Winner: " + str(n) + "squared total: " + str(total) + " " + str(time.time() - StartTime))
    n = n + 1
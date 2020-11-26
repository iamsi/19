#imports
import time
import sympy

StartTime = time.time()
CurrPrime = 2
n = 1
total = 0

while True:
    print (CurrPrime, end='\r')
    total = total + (CurrPrime ** 2)
    CurrPrime = sympy.nextprime(CurrPrime)
    if ( total % n == 0):
        print ("Winner: " + str(n) + "squared total: " + str(total) + " " + str(time.time() - StartTime))
    n = n + 1
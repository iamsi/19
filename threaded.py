#imports
import time
import sympy
from queue import Queue
from threading import Thread

def add_Primes(q):
    total = 0
    n = 1
    while True:
        x = q.get()
        total = total + (x ** 2)
        if ( total % n == 0):
            print ("Winner: " + str(n) + " squared total: " + str(total) + " " + str(time.time() - StartTime))
        n = n +1
        q.task_done()
q = Queue(maxsize=0)
StartTime = time.time()
CurrPrime = 2
worker = Thread(target=add_Primes, args=(q,))
worker.setDaemon(True)
worker.start()

q.put(2)
while True:
    CurrPrime = sympy.nextprime(CurrPrime)
    q.put(CurrPrime)
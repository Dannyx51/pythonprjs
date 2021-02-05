from random import vonmisesvariate
from secrets import *
from math import *
import time

st = time.time()
def nextInt(bit):
    p = 0
    while p % 2 == 0 or p % 5 == 0:
        p = randbits(bit)
    return p

def baseTwoTest(a):
    n = a - 1 
    while True:
        v = 2 ** n
        if v % a == 1:
            n //= 2
        elif v % a == a - 1: return True
        else: return False
        if n % 2 != 0:  return True
                                                

def newPrime(bit):
    a = nextInt(bit)


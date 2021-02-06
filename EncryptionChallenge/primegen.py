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
                                                
def JSymbol(n):
    D = 5
    count = 0
    while True:
        v = D
        v %= n
        ret = 1
        while v != 0:
            while v % 2 == 0:
                v //= 2
                temp = n % 8
                if temp in (3,5):
                    ret *= -1
            v, n = n, v
            if v % 4 == 3 and n % 4 == 3:
                ret *= -1
            v %= n
        
        if n == 1 and ret == -1:
            return D
        else: 
            if count % 2 == 0:
                D = (D + 2) * - 1
            else:
                i = abs(D) + 2
            count += 1
            

def newPrime(bit):
    while True:
        a = nextInt(bit)
        if not baseTwoTest(a): continue
        D = JSymbol(a)
        P = 1
        Q = (1-D)//4

        u1 = 1
        v1 = 1





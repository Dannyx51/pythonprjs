#test file to just try some algos and stuff without dealing with the rest of the project files
import time

def foo(m):
    global n
    n = m + 1
    print(n)
    foo(n)
    time.sleep(0.01)
n = 1
foo(n)
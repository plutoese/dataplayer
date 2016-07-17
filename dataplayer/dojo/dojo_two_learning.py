# coding = UTF-8

import time, sys

class tracer:
    def __init__(self, func):             # On @ decoration: save original func
        self.calls = 0
        self.func = func

    def __call__(self, *args, **kwargs): # On call to original function
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        return self.func(*args, **kwargs)

@tracer
def spam(a, b, c):           # spam = tracer(spam)
    print(a + b + c)         # Wraps spam in a decorator object

@tracer
def eggs(x, y): # Same as: eggs = tracer(eggs)
    print(x ** y) # Wraps eggs in a tracer object

spam(1, 2, 3) # Really calls tracer instance: runs tracer.__call__
spam(a=4, b=5, c=6) # spam is an instance attribute
eggs(2, 16) # Really calls tracer instance, self.func is eggs
eggs(4, y=4) # self.calls is per-decoration here


class timer:
    def __init__(self, func):
        self.func    = func
        self.alltime = 0
    def __call__(self, *args, **kargs):
        start   = time.clock()
        result  = self.func(*args, **kargs)
        elapsed = time.clock() - start
        self.alltime += elapsed
        print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
        return result

@timer
def listcomp(N):
    return [x * 2 for x in range(N)]

result = listcomp(5)                # Time for this call, all calls, return value
listcomp(50000)
listcomp(500000)
listcomp(1000000)
print(result)
print('allTime = %s' % listcomp.alltime)      # Total time for all listcomp calls



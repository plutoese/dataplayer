# coding=UTF-8

def f1(*args): print(args)

f1()
# ()
f1(2)
# (2,)
f1(1,2,3,4)
# (1, 2, 3, 4)


def f2(a, *pargs, **kargs): print(a, pargs, kargs)

f2(1, 2, 3, x=1, y=2)
# 1 (2, 3) {'x': 1, 'y': 2}

def func(a, b, c, d): print(a, b, c, d)
args = (1, 2)
args += (3, 4)
#func(args)
# func() missing 3 required positional arguments: 'b', 'c', and 'd'
func(*args)
# 1 2 3 4
func(*(1, 2), **{'d': 4, 'c': 3})
# Same as func(1, 2, d=4, c=3)


def mysum(L):
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

print(mysum([1, 2, 3, 4, 5]))
# 15

def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)

print(mysum(('s', 'p', 'a', 'm')))
# spam


def sumtree(L):
    tot = 0
    for x in L: # For each item at this level
        if not isinstance(x, list):
            tot += x # Add numbers directly
        else:
            tot += sumtree(x) # Recur for sublists
    return tot

print(sumtree([[[[[1], 2], 3], 4], 5]))
# 15


def make(label): # Make a function but don't call it
    def echo(message):
        print(label + ':' + message)
    return echo

F = make('Spam')
F('Eggs!')

'''
def fetcher(obj, index):
    return obj[index]

x = 'spam'
try:
    fetcher(x, 4)
except IndexError: # Catch and recover
    print('got exception')


try:
    raise IndexError # Trigger exception manually
except IndexError:
    print('got exception')


def after():
    try:
        fetcher(x, 4)
    finally:
        print('after fetch')
    print('after try?')

after()
# after fetch
# Traceback (most recent call last):'''

with open('lumberjack.txt', 'w') as file: # Always close file on exit
    file.write('The larch!\n')

'''
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self): # name = property(name) "name property docs"
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value): # name = name.setter(name)
        print('change...')
        self._name = value

    @name.deleter
    def name(self): # name = name.deleter(name)
        print('remove...')
        del self._name

bob = Person('Bob Smith') # bob has a managed attribute
print(bob.name) # Runs name getter (name 1)
bob.name = 'Robert Smith' # Runs name setter (name 2)
print(bob.name)
del bob.name # Runs name deleter (name 3)'''


class Catcher:
    def __getattr__(self, name):
        print('Get: %s' % name)
    def __setattr__(self, name, value):
        print('Set: %s %s' % (name, value))

X = Catcher()
X.job # Prints "Get: job"
X.pay # Prints "Get: pay"
X.pay = 99 # Prints "Set: pay 99"


class Person: # Portable: 2.X or 3.X
    def __init__(self, name): # On [Person()]
        self._name = name # Triggers __setattr__!

    def __getattr__(self, attr): # On [obj.undefined]
        print('get: ' + attr)
        if attr == 'name': # Intercept name: not stored
            return self._name # Does not loop: real attr
        else: # Others are errors
            raise AttributeError(attr)

    def __setattr__(self, attr, value): # On [obj.any = value]
        print('set: ' + attr)
        if attr == 'name':
            attr = '_name' # Set internal name
        self.__dict__[attr] = value # Avoid looping here

    def __delattr__(self, attr): # On [del obj.any]
        print('del: ' + attr)
        if attr == 'name':
            attr = '_name' # Avoid looping here too
        del self.__dict__[attr] # but much less common

print('---------start--------')
bob = Person('Bob Smith') # bob has a managed attribute
print(bob.name) # Runs __getattr__
bob.name = 'Robert Smith' # Runs __setattr__
print(bob.name)
del bob.name # Runs __delattr__


class GetAttr:
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattr__(self, attr): # On undefined attrs only
        print('get: ' + attr) # Not on attr1: inherited from class
        if attr == 'attr3': # Not on attr2: stored on instance
            return 3
        else:
            raise AttributeError(attr)

X = GetAttr()
print(X.attr1)
# 1
print(X.attr2)
# 2
print(X.attr3)
# get: attr3
# 3


class GetAttribute(object): # (object) needed in 2.X only
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattribute__(self, attr): # On all attr fetches
        print('get: ' + attr) # Use superclass to avoid looping here
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)

X = GetAttribute()
print(X.attr1)
# get: attr1
# 1
print(X.attr2)
# get: attr2
# 2
print(X.attr3)
# get: attr3
# 3

'''
class Powers(object): # Need (object) in 2.X only
    def __init__(self, square, cube):
        self._square = square # _square is the base value
        self._cube = cube # square is the property name

    def getSquare(self):
        return self._square ** 2

    def setSquare(self, value):
        self._square = value

    square = property(getSquare, setSquare)

    def getCube(self):
        return self._cube ** 3

    cube = property(getCube)

X = Powers(3, 4)
print(X.square) # 3 ** 2 = 9
print(X.cube) # 4 ** 3 = 64
X.square = 5
print(X.square) # 5 ** 2 = 25'''

'''
# Same, but with generic __getattr__ undefined attribute interception
class Powers:
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattr__(self, name):
        if name == 'square':
            return self._square ** 2
        elif name == 'cube':
            return self._cube ** 3
        else:
            raise TypeError('unknown attr:' + name)

    def __setattr__(self, name, value):
        if name == 'square':
            self.__dict__['_square'] = value # Or use object
        else:
            self.__dict__[name] = value

X = Powers(3, 4)
print(X.square) # 3 ** 2 = 9
print(X.cube) # 4 ** 3 = 64
X.square = 5
print(X.square) # 5 ** 2 = 25'''

'''
# Same, but with generic __getattribute__ all attribute interception
class Powers(object): # Need (object) in 2.X only
    def __init__(self, square, cube):
        self._square = square
        self._cube = cube

    def __getattribute__(self, name):
        if name == 'square':
            return object.__getattribute__(self, '_square') ** 2
        elif name == 'cube':
            return object.__getattribute__(self, '_cube') ** 3
        else:
            return object.__getattribute__(self, name)

    def __setattr__(self, name, value):
        if name == 'square':
            object.__setattr__(self, '_square', value) # Or use __dict__
        else:
            object.__setattr__(self, name , value)

X = Powers(3, 4)
print(X.square) # 3 ** 2 = 9
print(X.cube) # 4 ** 3 = 64
X.square = 5
print(X.square) # 5 ** 2 = 25'''


class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job  = job
        self.pay  = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)      # Embed a Person object
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)      # Intercept and delegate
#    def __getattr__(self, attr):
#        return getattr(self.person, attr)           # Delegate all other attrs
##    def __repr__(self):
##        return str(self.person)                     # Must overload again (in 3.X)
    def __getattribute__(self, attr):
        print('**', attr)
        if attr in ['person', 'giveRaise']:
            return object.__getattribute__(self, attr)   # Fetch my attrs
        else:
            return getattr(self.person, attr)            # Delegate all others

sue = Person('Sue Jones', job='dev', pay=100000)
print(sue.lastName())
sue.giveRaise(.10)
print(sue)
tom = Manager('Tom Jones', 50000)    # Manager.__init__
print(tom.lastName())                # Manager.__getattr__ -> Person.lastName
tom.giveRaise(.10)                   # Manager.giveRaise -> Person.giveRaise
print(tom)                           # Manager.__repr__ -> Person.__repr__


def inc(x):
    return x+1
    
def dec(x):
    return x-1
    
f = inc
print f(5)

flist = [inc, dec]
print flist[1](5)

def makeAdder(n):
    def inner(x):
        return x+n
    return inner
    
add3 = makeAdder(3)
add5 = makeAdder(5)

print add3(10)
print add5(10)





# A clunky approach to class type abstraction:
def make_counter():
    # private "instance" data
    # has to be a list due to weird python scoping rules
    count = [0]
    
    # public methods
    def inc():
        count[0] = count[0]+1
    def dec():
        count[0] = count[0]-1
    def reset():
        count[0] = 0
    def get():
        return count[0]
        
    #return a dictionary so we have access to all the methods
    return {'inc': inc, 'dec':dec, 'reset':reset, 'get':get}
    
c1 = make_counter()
c2 = make_counter()

# Must use clunky list notation:
c1['inc']()
c1['inc']()
c1['inc']()
print c1['get']()

c2['inc']()
print c2['get']()

c1['reset']()
print c1['get']()





# How is this useful?
# Suppose routines like the following, which returns a string:
#import random
#def get_name():
#    names = ['Tom', 'Sue', 'Harry', 'Lisa', 'Sarah', 'Horatio']
#    return random.choice(names)
    
# Suppose many calls to get_name throughout code.
# Suppose want to double name each time used.
# A "traditional" way of doing this might be:

def dble(f):
    name = f()
    return name+name
    
# THIS IS NOT A CLOSURE because no inner function is being defined





import random
def doubler(f):
    def inner():
        name = f()
        return name+name
    return inner

@doubler
def get_name():
    names = ['Tom', 'Sue', 'Harry', 'Lisa', 'Sarah', 'Horatio']
    return random.choice(names)
    
print get_name()

# 2nd eg will have demo return "hellohello" whenever we invoke it.
# equiv to:
#   get_name = double(get_name)
#
# TAKEAWAY:
# BAM!: can write functions that transform functions
#
# A Python decorator is merely shorthand for calling a wrapper-type function like doubler.
#
# A Python decorator encapsulates a closure
#
# A decorator allows to transparently wrap functionality
#
# You need ot define the inner function in order to use the decorator
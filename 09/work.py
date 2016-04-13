###############################################################################
#         HOMEWORK 9                HOMEWORK 9                HOMEWORK 9      #
#         HOMEWORK 9                HOMEWORK 9                HOMEWORK 9      #
#         HOMEWORK 9                HOMEWORK 9                HOMEWORK 9      #
#         HOMEWORK 9                HOMEWORK 9                HOMEWORK 9      #
###############################################################################
# Write a closure/decorator apparatus that will facilitate timing, and another
# for output of function name and arguments, and use decorators to apply one or 
# both of these to functions of your choosing. Store your work in hw09 subdir of
# your hw repo.
import time
import random

def timer(func):
    def clock():
        start = time.clock()
        # time.sleep(random.randint(0,2))
        func()
        end = time.clock()
        elapsed = end - start
        return elapsed
    return clock
        
def wuzzat(func):
    def that(*arg):
        return "Function Name: " + func.func_name + "\nArguments: " + ", ".join(str(e) for e in func(*arg))
    return that
        
def qsort(l):
    if(l==[]):
        return []
    lh = [x for x in l if x<l[0]]
    uh = [x for x in l if x>l[0]]
    return qsort(lh) + [l[0]] + qsort(uh)
    
@timer
@wuzzat
def test():
    return qsort([random.randint(0,50) for x in range(1,30)])
    
guinea_pig = test()
print guinea_pig

#def make_bold(fn):
#    return lambda : "<b>" + fn() + "</b>"
#
#def make_italic(fn):
#    return lambda : "<i>" + fn() + "</i>"
#
#@make_bold
#@make_italic
#def hello():
#    return "hello world"
#
#helloHTML = hello()
#
#print helloHTML

################################################################################

def name_log(f):
    def inner(*arg):
        t = time.time()
        x = f(*arg)
        print f.func_name + ": " + str(*arg)
        return x
    return inner

def timer2(f):
    def inner(*arg):
        t = time.time()
        x = f(*arg)
        print 'execution time: ' + str(time.time()-t)
        return x
    return inner
    
def randList(n, lower=-100, upper=100):
    l = []
    for i in range(n):
        l.append(random.randrange(lower,upper))
    return l
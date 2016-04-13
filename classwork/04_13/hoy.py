################################################################################
#                                                                              #
# DYNAMIC PROGRAMMING                                                          #
# aka "dynamic optimization"                                                   #
# means of solving a complex problem by solving its component subproblems just #
# once and storing their solutions                                             #
#                                                                              #
################################################################################
#                                                                              #
# MEMOIZATION                                                                  #
# technique of storing solutions to subproblems to avoid recomputation         #
# OR                                                                           #
# use of caches to retrieve previously computed values to reduce time          #
# complexity of algorithms                                                     #
#                                                                              #
################################################################################
#                                                                              #
# TASK:                                                                        #
# Rewrite fib(n) to employ dynamic programming                                 #
#                                                                              #
################################################################################

def fibo(n):
    if n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

previous = {}
def fib(n):
    if(n<2):
        return n
    else:
        if(n-1 not in previous.keys()):
            previous[n-1] = fib(n-1)
        if(n-2 not in previous.keys()):
            previous[n-2] = fib(n-2)
        return previous[n-1] + previous[n-2]
        
print "DYNAMIC: " + str(fib(1)) + " ; ORIGINAL: " + str(fibo(1))
print "DYNAMIC: " + str(fib(2)) + " ; ORIGINAL: " + str(fibo(2))
print "DYNAMIC: " + str(fib(3)) + " ; ORIGINAL: " + str(fibo(3))
print "DYNAMIC: " + str(fib(4)) + " ; ORIGINAL: " + str(fibo(4))
print "DYNAMIC: " + str(fib(5)) + " ; ORIGINAL: " + str(fibo(5))
print "DYNAMIC: " + str(fib(6)) + " ; ORIGINAL: " + str(fibo(6))
print "DYNAMIC: " + str(fib(7)) + " ; ORIGINAL: " + str(fibo(7))
print "DYNAMIC: " + str(fib(8)) + " ; ORIGINAL: " + str(fibo(8))
print "DYNAMIC: " + str(fib(9)) + " ; ORIGINAL: " + str(fibo(9))

def memoize(f):
    memo = {} #hashmap/dict for 0(1) lookup
    def inner(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return inner

def fib_d(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib_d = memoize(fib_d) #turn memoize into a decorator
print fib_d(0)
print fib_d(1)
print fib_d(2)
print fib_d(3)
print fib_d(4)
print fib_d(5)
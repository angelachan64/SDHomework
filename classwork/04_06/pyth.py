###############################################################################
#         PYTH ONE                PYTH ONE                PYTH ONE            #
#         PYTH ONE                PYTH ONE                PYTH ONE            #
#         PYTH ONE                PYTH ONE                PYTH ONE            #
#         PYTH ONE                PYTH ONE                PYTH ONE            #
###############################################################################
def pt(n):
#    nums = []
#    odd = []
#    count = 1
#    while(count<=n**2):
#        nums.append(count)
#        count += 1
#    for x in nums:
#        if x%2==1:
#            odd.append(x)
#    print odd

    retl = []
    for a in range(1,n):
        for b in range(a,n):
            for c in range(b,n):
                if (a*a + b*b == c*c):
                    retl.append([a,b,c])
    return retl
    
print pt(3)
print pt(9)
print pt(50)




###############################################################################
#         PYTH TWO                PYTH TWO                PYTH TWO            #
#         PYTH TWO                PYTH TWO                PYTH TWO            #
#         PYTH TWO                PYTH TWO                PYTH TWO            #
#         PYTH TWO                PYTH TWO                PYTH TWO            #
###############################################################################
def pt2(n):
#    lists = []
#    ret = []
#    for a in range(1,n):
#        for b in range(1,n):
#            for c in range(1,n):
#                if(a<b & b<c):
#                    lists.append([a,b,c])
#    ret = [x for x in lists if x[0]*x[0] + x[1]*x[1] == x[2]*x[2]]
#    return ret
    return [(a,b,c)
            for a in range(1,n)
            for b in range(a,n)
            for c in range(b,n)
            if (a**2 + b**2 == c**2)]


    
print pt2(3)
print pt2(9)
print pt2(50)




###############################################################################
#         QUICKSORT                QUICKSORT                QUICKSORT         #
#         QUICKSORT                QUICKSORT                QUICKSORT         #
#         QUICKSORT                QUICKSORT                QUICKSORT         #
#         QUICKSORT                QUICKSORT                QUICKSORT         #
###############################################################################
# 1. PICK A PIVOT
# 2. PARTITION into 2 lists
#    a. all points<pivot are LH
#    b. all points>pivot are UH
#    c. PIVOT in right position
# 3. QSort right & left hand sides
# WRITE THIS WITH LISTCOMP
def qsort(l):
    lh = [x for x in l if x<l[0]]
    uh = [x for x in l if x>l[0]]
    qsort(lh)
    qsort(uh)
    return lh + l[0] + uh
    
import random
lnums = [random.randint(1,100) for x in range(1,20)]
#qsort(lnums)
print lnums

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
import time

def qsort(l):
    if(l==[]):
        return []
    lh = [x for x in l if x<l[0]]
    uh = [x for x in l if x>l[0]]
    return qsort(lh) + [l[0]] + qsort(uh)
    
import random
lnums = [random.randint(1,100) for x in range(1,20)]
print lnums
print qsort(lnums)


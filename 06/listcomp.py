UC_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lc_letters = "abcdefghijklmnopqrstuvwxyz"
numbers    = "0123456789"
pass1      = "likliklik"
pass2      = "Likliklik"
pass3      = "likliklik123"
pass4      = "LIKLIKLIK123"
pass5      = "Likliklik123"
pass6      = "LikLiKLik12345L"

def pass_test(password):
    print (not((not[x for x in password if x in UC_LETTERS]) or (not[x for x in password if x in lc_letters]) or (not[x for x in password if x in numbers])))
    
pass_test(pass1)
pass_test(pass2)
pass_test(pass3)
pass_test(pass4)
pass_test(pass5)

def pass_strength(password):
    strength = 0
    uletters = [x for x in password if x in UC_LETTERS]
    lletters = [x for x in password if x in lc_letters]
    pnums    = [x for x in password if x in numbers]
    if ((len(uletters) == len(lletters)) & (len(uletters) == len(pnums))):
        print "10"
    else:
        strn = (len(pnums)+len(uletters)-len(lletters))
        if (strn<0 & strn > -10):
            print 10+strn
        elif (strn>10):
            print strn-10
        else:
            print abs(strn)
        
pass_strength(pass1)
pass_strength(pass2)
pass_strength(pass3)
pass_strength(pass4)
pass_strength(pass5)
pass_strength(pass6)
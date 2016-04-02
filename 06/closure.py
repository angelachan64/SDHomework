def repeat(string):
    def times(num):
        return string*num
    return times
        
r1 = repeat("hello")
r2 = repeat("goodbye")

print r1(2)
print r2(2)
print repeat("cool")(3)

#Multiply both numbers until there is a common multiple and then break. Use if else and while inside a method.

"""def lcmFunction(x,y):
    a = 0
    b = 0
    c = 0
    d = 0
    z = 0
    while(z == 0):
        c = x*(a+1)
        d = y*(b+1)
        if(c == d):
            z = c
            return z
"""


            
def lcmFunction(x,y):
        a=1
        b=1
        for i in range(10):
            c = x*(a)
            a+=1
            
            d = y*(b)
            b+=1
            
            if ((d%x) == 0):
                
                return d
                break
            elif ((c%y) == 0):
                
                return c
                break


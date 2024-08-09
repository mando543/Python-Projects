# Find the product of x and y. Find the LCM of x and y. Divide the product by the LCM to find GCD.

import lcmFunction

def gcdFunction(d, e):
    a = d * e
    b = lcmFunction.lcmFunction(d, e)
    c = a/b
    return c

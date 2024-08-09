# Function that takes a string as a parameter.
# Function must reverse string by converting string to list
#Then use :: or .reverse() to reverse
#Convert list to string

def reverseString(String):
    a = list(String)
    b = a[::-1]
    #return b
    str = ""
    for i in b:
        str += i
    return str

    
    
    

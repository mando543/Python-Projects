#Write program that determines whether or not "cat" and "dog" appear the same number of times in given string
#Use user input, for loops, if&else, and searching









def findWords():
    
    String = str(input("Please enter a string with the words \"cat\" and \"dog\" in it: "))
    catCounter = 0
    dogCounter = 0
    totalCounter = 0

    #for i in String:
    
    if "cat" or "Cat" in String:
        catCounter = catCounter + 1
        print("catCounter: "+str(catCounter))

    if "dog" or "Dog" in String:
        dogCounter = dogCounter + 1
        print("dogCounter: "+str(dogCounter))
    
    if catCounter == dogCounter:
        totalCounter = totalCounter + 1
        print("totalCounter: "+str(totalCounter))
        
    else:
        print("The words \"cat\" and \"dog\" do not appear the same amount of times in this string")


    finalCounter = str(totalCounter)
    print("finalCounter: "+finalCounter)

    
    print("The words \"cat\" and \"dog\" have both appeared " +finalCounter +" times in this string.")

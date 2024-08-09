#Write function that:
#Option 1 - no parameter, just asks user input for both string and shift
#Option 2 - Takes String as parameter and asks user for shift

import string



#Testing Option 1
def caesarDecipher():
    alphabets = list(string.ascii_letters)

    String = list(input("Please enter the Caesar Cipher string you would like to decrypt: "))
    shift = int(input("Please enter the shift number from the sender: "))



    newString = ""
    
    for i in String:
        if i in alphabets:
            oldIndex = alphabets.index(i)
            #print("This is the index value of the letter in ascii: "+str(oldIndex))
            newIndex = oldIndex - shift
            #print("This is the shifted index in ascii: "+str(newIndex))
            newLetter = str(alphabets[newIndex])
            #print("This is the value of the shifted index in ascii: "+newLetter)
            #print("Why isn't "+newLetter +" showing up in the next line?")
            newString = newString + newLetter
            #print(newString)
            #print("^This is the encrypted form of: "+i)
        else:
            print(i + " is not a letter in the English alphabet")

    print("Here is your decrypted string: "+newString)

    

    
            
    #finalString = str(newString)
    #return finalString

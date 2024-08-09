a = int(input("Please input the first number: ")) # input a float value for variable a here
b = int(input("Please input the second number: ")) # input a float value for variable b here


print(a ,"+", b, "=" ,a+b) # output the result of addition here
print(a ,"-", b, "=" ,a-b) # output the result of subtraction here
print(a ,"*", b, "=" ,a*b) # output the result of multiplication here
if b == 0:
    print(a ,"/", b, "= undefined" ,"\nSorry, you cannot divide by zero. Please try again.")
    exit()
else:
    print(a ,"/", b, "=" ,round((a/b),2)) # output the result of division here


print("That's all, folks!")

# import sys so I can use sys.argv
import sys

# assign variables the first three command line
# arguments after the name
num1= float (sys.argv[1])
num2= float (sys.argv[2])
num3= float (sys.argv[3])

# add variables together and store in result
result= num1 + num2 + num3

# print result
print(num1, "+", num2, "+", num3, "=", result)
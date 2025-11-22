# Author : Manpreet Kaur
# Basic calculator program

'''
This is a basic calculator program which takes two numbers as an input from the user
along with the operator of the operation that user want to perform and returns the output.
'''

print("Welcome! to the calculator")
print("operations the this calculator can perform and their corresponding operators:")
print(" + : Addition")
print(" - : Subtraction")
print(" * : Multiplication")
print(" / : Division")
print(" // : Floor Division")
print(" ** : Exponention")

num1=float(input("Enter first number:"))   # taking input for first number from user
num2=float(input("Enter second number:"))  # taking input for secong number from user
operator=input("Enter the operator:")

# conditional statements or comparison part

if operator=="+":  
    add=num1+num2  # performing the addition 
    print("Addition of",num1,"and",num2,":",add)   # printing the result

elif operator=="-":
    sub=num1-num2   # performing the subtraction
    print("Subtration of",num1,"and",num2,":",sub)   # printing the result

elif operator=="*":
    mul=num1*num2    # performing the multiplication
    print("Multiplication of",num1,"and",num2,":",mul)   # printing the result

elif operator=="/":
    divi=num1/num2    # performing the division
    print("Division of",num1,"and",num2,":",divi)   # printing the result

elif operator=="**":  
    exp=num1**num2   # performing the exponention
    print(num1,"to the power",num2,":",exp)   # printing the result

elif operator=="//":
    floor_div=num1//num2    # performing the floor division
    print("Floor division of",num1,"and",num2,":",floor_div)   # printing the result

else: 
    print("you entered the wrong operator !!")   # if operator doesnot match then printing the error message

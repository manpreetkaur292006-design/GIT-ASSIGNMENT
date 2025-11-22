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

num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
operator=input("Enter the operator:")

if operator=="+":
    add=num1+num2
    print("Addition of",num1,"and",num2,":",add)

elif operator=="-":
    sub=num1-num2
    print("Subtration of",num1,"and",num2,":",sub)

elif operator=="*":
    mul=num1*num2
    print("Multiplication of",num1,"and",num2,":",mul)

elif operator=="/":
    divi=num1/num2
    print("Division of",num1,"and",num2,":",divi)

elif operator=="**":
    exp=num1**num2
    print(num1,"to the power",num2,":",exp)

elif operator=="//":
    floor_div=num1//num2
    print("Floor division of",num1,"and",num2,":",floor_div)

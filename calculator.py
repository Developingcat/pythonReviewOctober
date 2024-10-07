"""
Author: Hannah O'Shea 
Program: Calculator.py

Function for basic_arithmetic for the two numbers 

Make sure the numbers are input from the user 

A string consisting of either multiplication, division, subtraction or addition  

Something like: 

int(input("Please select the number you'd like to (math function) here."))

If statements if possible based overall on how to do it, would also be neat 
Like "if user input= additon" then it leads to the additional equations

"""

 



# Multiplication
def multiply():
    lower = int(input("Please enter the lower bound number!"))
    upper = int(input("Please enter the upper bound number!"))


    x = lower
    y = upper

    theProduct = ( x*y )
    for number in range(lower * upper, upper):
        theProduct *= number (x*y)
    print(theProduct)


# Subtraction 
def subtraction():
    lower = int(input("Please enter the number you'd like to subtract!: "))
    upper = int(input("Please enter the number you'd like to subtract from!: "))

    a = lower 

    b = upper 

    theSub = (a-b)

    for number in range(lower, upper - lower):
        theSub -= number(a-b)
    print(theSub)


# # Addition 
def addition():
    lower = int(input("Please enter the number you'd like to add!: "))
    upper = int(input("Please enter the other number you'd like to add!: "))

    c = lower 

    d = upper 

    theSum = (c+d)

    for number in range(lower + upper, upper):
        theSum += number(c+d)
    print(theSum)


# # Divison 

def divison():
    lower = int(input("Please enter the number you'd like to divide!: "))
    upper = int(input("Please enter the other number you'd like to divide!: "))

    e = lower 

    f = upper 

    theDivider = (e//f)

    for number in range(lower, upper//lower):
        theDivider /= number(e//f)
    print(theDivider)


answer = input("Choose between what you want to do NOW; addition, subtraction, divison, multiply ")
if answer == "addition":
    addition()
if answer == "subtraction":
    subtraction()
if answer == "divison":
    divison()
if answer == "multiply":
    multiply()

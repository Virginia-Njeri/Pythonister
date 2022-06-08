# Exercise 1: Define a function that accepts 2 
# values and return its sum, subtraction and multiplication.
from re import A


def numbers(a,b):
    product=a*b
    addition=a+b
    subtraction=a-b
    print(product,subtraction,addition)
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))   
numbers(a,b)
# Exercise 2: Define a function that accepts roll number
#  and returns whether the student is present or absent.

def roll_call(call):
    call=int(input("please enter you number"))
    roll_numbers=[12,13,14,15,16,17,18]

    
'''
Design a function that prints the even numbers in a range of numbers.
'''
'''
def even(n):
    for number in range(1, n+1):
        if number%2 == 0:
            print(number, "is even")

even(100)
'''

# function that returns the sum of two numbers
'''
def sum_of_numbers(x, z):
    x = input(int("Enter a number:"))
    y = input(int("Enter a second number:"))
    z = input(int("Enter a third number:"))
    return x+y+z
'''

import turtle as t
def drawRectangle(t,w,h):
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)

drawRectangle(t,100,50)

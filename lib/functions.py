#!/usr/bin/env python3

def greet_programmer():
    print("Hello programmer!")
 
greet_programmer()   



def greet(name):
    print(f"Hello,{name}")

greet("James")

def greet_with_default(name="programmer"):
    print(f"Hi, {name}")

greet_with_default()    

def add(num1, num2):
    return num1 + num2
   



print(add(5,8))

def halve(number):
    return number/2

print(halve(12))



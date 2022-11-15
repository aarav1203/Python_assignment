# 1. Write a Python program to convert kilometers to miles?

def kmtomile(ip):
    return(ip/1.60934)

ip=6
ans=kmtomile(ip)
print(f"km: {ip} and miles: {ans}")    

# 2.Write a Python program to convert Celsius to Fahrenheit?

def celFah(ip):
    return(9*ip/5+32)

ip=35
ans=celFah(ip)
print(f"celsius: {ip} and fahreheit: {ans}")    

# 3. Write a Python program to display calendar?

import calendar

def cal(yr,mth):
    return calendar.month(yr,mth)

yr=2022
mth=11
ans=cal(yr,mth)
print(f"month calendar is {ans}")    

# 4. Write a Python program to solve quadratic equation?

import math

def quad(a,b,c):
    exp=math.sqrt((b**2)-(4*a*c))
    root1=(-1*b+exp)/2*a
    root2=(-1*b-exp)/2*a
    return (f"one root is : {root1} and other root is : {root2}")
a=int(input("Enter value of a"))
b=int(input("Enter value of b"))
c=int(input("Enter value of c"))
print(quad(a,b,c))

# 5. Write a Python program to swap two variables without temp variable?

def swap(a,b):
    a=a+b
    b=a-b
    a=a-b
    return(f"After swapping value of a is {a} and value of b is {b}")

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))    
print(f"Before swapping value of a is {a} and value of b is {b}")
print(swap(a,b))
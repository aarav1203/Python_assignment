# 1. Write a Python Program to Find the Factorial of a Number?

def fact(n):
    f=1
    while(n>1):
        f*=n
        n=n-1
    return f

ip=int(input("enter value: "))
print(fact(ip))        

# 2. Write a Python Program to Display the multiplication Table?

def mul(n):
    for num in range(1,11):
        print(f"{n} x {num} = {n*num}")
ip=int(input("input number: "))
mul(ip)        

# 3. Write a Python Program to Print the Fibonacci sequence?

def fib(n):
    val1=0
    val2=1
    print(val1,end=' ')
    print(val2,end=' ')
    sum=0
    while(n-2>0):
        sum+=val1+val2
        print(sum,end=' ')
        n-=1

ip=int(input("Enter the number: "))
fib(ip)

# 4. Write a Python Program to Check Armstrong Number?
def arm(ip):
    temp=ip
    op=0
    while(temp>0):
        rem=temp%10
        op=op+(rem**3)
        temp=temp//10
    if op==ip:
        print(f"{ip} is armstrong number") 
    else:
        print(f"{ip} is not armstrong number")       

ip=int(input("enter the number: "))
print(arm(ip))        

# 5. Write a Python Program to Find Armstrong Number in an Interval?
def arm(ip):
    temp=ip
    op=0
    while(temp>0):
        rem=temp%10
        op=op+(rem**3)
        temp=temp//10
    if op==ip:
        return(True)
       
    else:
        return(False)
          
def armint(start,end):
    for num in range(start,end):
        if arm(num):
            print(num ,end=' ')
ip1=int(input("Enter the start number: "))
ip2=int(input("Enter the last number: "))

armint(ip1,ip2)            
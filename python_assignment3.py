# 1. Write a Python Program to Check if a Number is Positive, Negative or Zero?

def chk(ip):
    if ip>0:
        return(f"{ip} is positive")
    elif ip<0:
        return(f"{ip} is negative")
    else:
        return(f"{ip} is zero")        

ip=int(input("Enter the number: "))
print(chk(ip))     

# 2. Write a Python Program to Check if a Number is Odd or Even?
def chkno(ip):
    if ip & 1==0:
        return(f"{ip} is even number")
    else:
        return(f"{ip} is odd number")    
ip=int(input("enter the number: "))
print(chkno(ip)) 

# 3. Write a Python Program to Check Leap Year?
def chk_year(ip):
    if(((ip % 4 == 0) and (ip % 100 != 0)) or (ip % 400 == 0)):
        print("Leap year")

    else:
        print("not leap year")

ip=int(input("Enter the year: "))
chk_year(2016)

# 4. Write a Python Program to Check Prime Number?     

def chkPrime(ip):
    if ip<=1:
        return(f"{ip} is neither prime nor composite number")
    rng=int(ip/2)
    for num in range(2,rng+1):
        if ip%num==0:
            return(f"{ip} is composite number")
            
    return(f"{ip} is prime number")

ip=int(input("Enter the number"))
print(chkPrime(ip))    

# 5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
def chkPrime(ip):
    if ip<=1:
        return(False)
    rng=int(ip/2)
    for num in range(2,rng+1):
        if ip%num==0:
            return(False)
            
    return(True)

for num in range(1,10001):
    if chkPrime(num):
        print(num,end=' ')   

import math 

def isPrime(n):
    if n < 2:  
        return "Not prime"
    if n == 2: 
        return "Prime"
    if n % 2 == 0: 
        return "Not prime"

    i = 3
    while i * i <= n:
        if n % i == 0:
            return "Not prime"
        i += 2

    
    return "Prime"

T = int(input()) 
for _ in range(T):
    n = int(input()) 
    print(isPrime(n)) 

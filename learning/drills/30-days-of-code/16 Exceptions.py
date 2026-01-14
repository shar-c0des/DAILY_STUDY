import sys 


S = input().strip()

try:
    # convert string to integer
    num = int(S)
    #print if successful
    print(num)
except ValueError:
    #if fails: exceute this
    print("Bad String")



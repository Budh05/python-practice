
#!sum of n nat no
def sum(n):
    if n==0: 
        print("The no. entered is not a nat. no.")
    elif n==1:
        return 1
    else:
        return n+sum(n-1)
n=int(input("enter a nat. no:"))
print("the sum of first n no. is ",sum(n))

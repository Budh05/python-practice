"Q) check whether the given no is prime"
m=int(input("enter no"))
if m<=1:
    print("The given digit is 0")
else:
    for i in range (2,m):
        if m%i==0:
            print("its not a Prime No.")
            break        
    else:
            print("Its a Prime No")
"print "
"*"
"**"
"***"
n=int(input("enter no"))
for i in range (1,n+1):
    print(("*"*i)+""*(n-i))

''' 2) prog print       
***
* *
*** '''
n=(int(input("enter no")))
for i in range (1,n+1):
    if i==1 or i==n:
        print("*"*n)
    else:
        print("*" + " " * (n - 2) + "*")

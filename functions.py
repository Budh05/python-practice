
            #!definnation of fn 
def avg(): 
    a=int(input("enter the no of elements:"))
    b=int(input("enter the elements:"))
    c=int(input("enter the elements:"))
    average=(a+b+c)/3
    print("the average of the given no is:",average)
avg()           #?calling fn
avg()

#*Q) greet user with hellp with fn
def greet():
    user=input("enter your name:")
    print("hello",user)
greet()
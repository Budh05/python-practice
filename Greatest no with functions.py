
#!greatest no with fn
def great():
    a= int(input("enter the 1st no:"))
    b= int(input("enter the 2nd no:"))
    c= int(input("enter the 3rd no:"))
    if (a>b and a>c):
        print("the greatest no is:",a)
    elif (b>a and b>c):
        print("the greatest no is:",b)
    else:
        print("the greatest no is:",c)
great()
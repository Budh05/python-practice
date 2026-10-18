
#!convert inches to cm
def cm (n):
    if n==0:
        return 0
    else:
         return n*2.54
n=float(input("ENter no of inches to convert"))
print(cm(n),"cm")

#!create a list of 4 and give the sum 
num=[2,3,55,5]
print(sum(num))

#*by input and for loop
num=[]
for i in range(4):
    n=int(input(f"enter no{i+1}\n"))
    num.append(n)
print("list of given no",num)
print("the sum")
print(sum(num))


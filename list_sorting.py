"display marks of 6 students in sorted "

        #* can done by 2 ways
    #? 1st)
marks=[]

m1=input("enter marks of student 1\n")
m2=input("enter marks of student 2\n")
m3=input("enter marks of student 3\n")
m4=input("enter marks of student 4\n")
m5=input("enter marks of student 5\n")
m6=input("enter marks of student 6\n")
marks=[m1,m2,m3,m4,m5,m6]
print(marks)
print("sorted\n")
marks.sort()
print(marks)

#? by for loop
marks=[]
for i in range (6):
    m=int(input(f"enter marks of student{i+1}: "))
    marks.append(m)

marks.sort()
print(marks)
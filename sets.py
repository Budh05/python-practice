"code to input 8 no from user and display only once"
        #?only onlce disply so use set 
n=set()
for i in range (8):
    s=int(input(f"enter no.s {i+1}:"))
    n.add(s)
print("the given no are")
print(n)

#! 3) find length of follwing code 
s=set()
s.add(20)
s.add(20.0)
s.add("20")
#? finding length
print("the length is =")
print(len(s))
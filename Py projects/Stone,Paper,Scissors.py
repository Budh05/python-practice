import random
choices={1:"rock ",2:"paper",3:"scissors"}
computer= random.randint(1,3)
user= int(input("enter your choice \nrock:1 \npaper:2\nscissors:3\n"))
print("computer choice=",choices[computer])
print("user choice=",choices[user])
if user== computer:
    print("DRAW")
elif (user==1 and computer==3)or (user==2 and computer==1) or(user==3 and computer==2):
    print("YOU WIN")
else:
    print("YOU LOSE,COMPUTER WON")


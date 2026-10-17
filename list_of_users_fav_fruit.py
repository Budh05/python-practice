"q1) create list with user input for 7 fruits "
    #todo cam be solved 3 ways
        #! 1)
print("enter 7 fruits name")
Fruit=[]
Fruit = []

f1 = input("Enter fruit 1: ")
Fruit.append(f1)

f2 = input("Enter fruit 2: ")
Fruit.append(f2)

f3 = input("Enter fruit 3: ")
Fruit.append(f3)

f4 = input("Enter fruit 4: ")
Fruit.append(f4)

f5 = input("Enter fruit 5: ")
Fruit.append(f5)

f6 = input("Enter fruit 6: ")
Fruit.append(f6)

f7 = input("Enter fruit 7: ")
Fruit.append(f7)

print(Fruit)

        #* 2)
f1 = input("Enter fruit 1: ")
f2 = input("Enter fruit 2: ")
f3 = input("Enter fruit 3: ")
f4 = input("Enter fruit 4: ")
f5 = input("Enter fruit 5: ")
f6 = input("Enter fruit 6: ")
f7 = input("Enter fruit 7: ")

Fruit = [f1, f2, f3, f4, f5, f6, f7]
print(Fruit)

        #? 3)for loop
Fruit=[]
for i in range(7):
    f= input(f"enter fruit {i+1}:")
    Fruit.append(f)

print(Fruit)
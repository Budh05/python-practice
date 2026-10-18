j=input('''temperature converter, enter what you want to convert:
a. farenheit to celsius
b. celsius to farenheit
''')
if j=='a':
    def temp(n):
        return (n-32)*5/9
    n=int(input("enter temp in farenheit:"))
    print("after converting into celsius, the temp is:",temp(n))
elif j=='b':
    def temp(n):
        return (n*9/5)+32
    n=int(input("enter temp in celsius:"))
    print("after converting into farenheit, the temp is:",temp(n))
else:
    print("invalid input")
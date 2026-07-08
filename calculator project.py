def sum(a,b):
    return (a + b)
def substract(a,b):
    return(a - b)
def multiply(a,b):
    return(a * b)
def divide(a,b):
    return(a / b)

#main

choice = int(input("1. Add\n2. Substract\n3. Multiply\n4. Divide\nChoose a number:"))

if choice == 1:
    fn = int(input("First number:"))
    fs = int(input("Second number:"))
    print("result:",sum(fn,fs))
elif choice == 2:
    fn = int(input("First number:"))
    fs = int(input("Second number:"))
    print("result:",substract(fn,fs))
elif choice == 3:
    fn = int(input("First number:"))
    fs = int(input("Second number:"))
    print("result:", multiply(fn,fs))
elif choice == 4:
    fn = int(input("First number:"))
    fs = int(input("Second number:"))
    print("result:", divide(fn,fs))
else:
    print("error try again")
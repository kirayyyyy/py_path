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

if choice in [1,2,3,4]:
    fn = int(input("First number:"))
    fs = int(input("Second number:"))
    if choice == 1:
        print("result:",sum(fn,fs))
    elif choice == 2:
        print("result:",substract(fn,fs))
    elif choice == 3:
        print("result:", multiply(fn,fs))
    elif choice == 4:
        print("result:", divide(fn,fs))
else:
    print("error try again")

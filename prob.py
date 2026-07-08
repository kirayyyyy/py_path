limit = int(input("what is the limit :"))
first = int (input("Enter the first number: "))
second = int(input("Enter the second number: "))
largest = first
secondlarge = second
if secondlarge > largest:
    largest = second
    secondlarge = first
for _ in range (limit - 2):
    number = (int(input("Enter number :")))
    if number > largest:
        secondlarge = largest
        largest = number

    else:
        if number > secondlarge:
            secondlarge = number
print ("largest :",largest)
print ("secondlarge :",secondlarge)
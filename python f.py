limit = int(input("what is the limit :"))
first = int (input("Enter the first number: "))
largest = first
smallest = first
sum = first
for _ in range (limit - 1):
    number = (int(input("Enter number :")))
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
    sum += number
average = sum / limit
print ("largest :",largest)
print ("smallest :",smallest)
print ("sum :",sum)
print ("average:",average)
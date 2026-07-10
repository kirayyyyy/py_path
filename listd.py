value = []
add = 0
for _ in range (0, 5):
    numbers = int(input("enter a number :"))
    value.append(numbers)
    add += numbers
largest = value[0]
smallest = value[1]
if smallest > largest:
    largest = value[0]
    smallest = value [0]
n = 2
x = value[n]
while n < 4:
    if largest < x:
        largest = x
    if smallest > x:
        smallest = x
    x = value[n+1]
    n += 1
average = add / (n+1)
print ("smallest:", smallest)
print ("largest:", largest)
print ("sum:", add)
print ("average:", average)
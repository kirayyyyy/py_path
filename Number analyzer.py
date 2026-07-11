numbers = []
nume = 1
if nume != 0:
    while nume != 0:
        nume = int(input("Enter number(number 0 end): "))
        if nume != 0:
            numbers.append(nume)
    print("Numbers: ")
    for nume in numbers:
                print (nume)
    largest = nume
    for nume in numbers:
        if largest <= nume:
            largest = nume
    print ("Largest:", largest)
    smallest = nume
    for nume in numbers:
        if smallest >= nume:
            smallest = nume
    print ("Smallest:", smallest)
    add = 0
    for o in range(len(numbers)):
        if len(numbers) == 0:
             print ("there is no average with 0")
             break
        else:
            add += numbers[o]
        average = add / len(numbers)
    print("Average:",average)
    even = 0
    odd = 0
    for nume in numbers:
        if nume % 2 == 0:
            even+= 1
        else:
            odd += 1
    print ("Even Numbers:",even)
    print ("Odd Numbers:",odd)
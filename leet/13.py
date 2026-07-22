numbers = [1,9,9]
l  = len(numbers) - 1
numbers [l] += 1
if numbers[l] > 9:
    if l == 0:
        numbers.append(numbers[l] % 10)
        numbers[l] = numbers[l] // 10    
    elif l > 0:
        while numbers[l] > 9:
            numbers[l] %= 10
            l-=1
            numbers[l] = numbers[l] + 1
print (numbers)
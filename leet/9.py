num = 1534236469
number = 0
i = 0
k = 0
b = 1
d = 1
negative = False
if num == 0:
    print (number)
else:
    while num % 10 == 0:
        num //= 10
    if num < 0:
        num *= -1
        negative = True
    lenght = len(str(num))
    while d != lenght:
        b*= 10
        d+= 1
    while k != lenght:
        digit = num % 10
        number += digit * b
        b //= 10
        k+= 1
        num //= 10
    if negative == True:
        number *= -1
    if number > 2147483647 or number < -2147483648:
        number = 0
    print (number)
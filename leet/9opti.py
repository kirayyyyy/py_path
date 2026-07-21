num = -137

negative = num < 0
num = abs(num)

while num != 0 and num % 10 == 0:
    num //= 10

reversed_num = 0

while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num //= 10

if negative:
    reversed_num *= -1

if reversed_num < -2147483648 or reversed_num > 2147483647:
    reversed_num = 0

print(reversed_num)
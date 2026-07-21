n = 234
multi = 1
sum = 0
d = n
while d > 0:
    b = d % 10
    multi *= b
    d //= 10 
while n > 0:
    b = n % 10
    sum += b
    n //= 10 
print(multi - sum)
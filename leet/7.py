def digit_sum(number):
    sum = 0
    while number != 0:
            digit = number % 10
            sum += digit
            number //= 10
    print(sum)
digit_sum(431)
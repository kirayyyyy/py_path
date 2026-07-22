dic = {
    "I" : 1,
    "V" : 5,
    "X" : 10,
    "L" : 50,
    "C" : 100,
    "D" : 500,
    "M" : 1000,
}
s = "MCMXCIV"
sum = 0
previous = "l"
for char in s:
    if previous == "I":
        if char == "V" or char == "X":
            sum-= 2
    if previous == "X":
        if char == "L" or char == "C":
            sum-= 20
    if previous == "C":
        if char == "D" or char == "M":
            sum-= 200
    previous = char
    sum += dic[char]
print(sum)
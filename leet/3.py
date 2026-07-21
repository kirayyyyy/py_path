accounts = [[2,8,7],[7,1,3],[1,9,5]]
cal = 0
sum = 0
for b in range(len(accounts)):
    for i in range(len(accounts[b])):
        cal += accounts[b][i]
    if cal > sum:
        sum = cal
    cal = 0
print(sum)
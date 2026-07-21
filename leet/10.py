matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
rotation = []
k = 0
l = len(matrix) - 1
i = l
for p in range(len(matrix[0])):
    while k <= p:
        rotation.append([])
        while l >= 0:
            rotation[k].append(matrix[l][k])
            l-= 1
        l = i
        k+=1
k = 0
j = 0
while k<l + 1:
    while j < l+1:
        matrix[k][j] = rotation[k][j]
        j += 1
    j = 0
    k+= 1
print(matrix)
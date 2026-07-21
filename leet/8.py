arr = [1,2,34,3,4,5,7,23,12]
i = 0
b = 0
for o in arr:
        if b == 3:
              break
        
        elif o % 2 != 0:
                b += 1
        else:
              b == 0
if b == 3:
    print(True)
else:
    print(False)
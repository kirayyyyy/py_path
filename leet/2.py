nums = [5,4,2,3]
arr = []
while nums:
    alice = min(nums)
    nums.remove(alice)

    bob = min(nums)
    nums.remove(bob)

    arr.append(bob)
    arr.append(alice)
print(arr)
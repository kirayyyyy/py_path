nums = [1,15,6,3]
sum = 0
sumd = 0
for i in range(len(nums)):
    sum += nums[i]
for o in range(len(nums)):
        while nums[o]  != 0:
            digit = nums[o] % 10
            sumd += digit
            nums[o] //= 10
print(sum - sumd)
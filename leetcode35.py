nums = [1,3,5,6]
target = 2

if target in nums:
    for i in range(0, len(nums)):
        if target == nums[i]:
            print(i)
else:
    nums.append(target)
    new = sorted(nums, key = lambda i:i, reverse=False)
    for i in range(0, len(new)):
        if target == new[i]:
            print(i)
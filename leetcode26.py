nums = [0,0,1,1,1,2,2,3,3,4]
#nums = [1,1,2]

# new = []
# for item in nums:
#     if item not in new:
#         print("item is ",item)
#         new.append(item)
# print(new)
slow, fast = 0, 1
for j in range(1,len(nums)):
    if nums[j] != nums[slow]:
        slow += 1
        nums[slow] = nums[j]
print(slow+1)

# while fast < len(nums):
#     if nums[fast] != nums[slow]:
#         slow = slow + 1
#         nums[slow] = nums[fast]
#     fast = fast + 1
# print(slow+1)
# return slow + 1
#
#
# l = len(nums)
# nums.extend(sorted(list(set(nums))))
# del nums[0:l]
# return len(nums)
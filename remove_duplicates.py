import time

nums_unsort = [1,1,2,4,5,6,5,3,5,2,5,5,5,3,6,2,6,4,5,6,2,2,2,3,4,2,1,4,4,1,2,5,3]
nums = sorted(nums_unsort)
print nums
upto_num = len(nums)
unique = []

for i in range(upto_num):
	j = i+1
	if j < upto_num:
		compare = cmp(nums[i],nums[j])
		if compare == -1:
			unique.append(nums[i])
	elif j == upto_num:
		unique.append(nums[j-1])

print unique

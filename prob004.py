#find the lowest positive integer that does not exist in the array. 

def find(array):
	
	if not array:
		return 1

	i=0
	while i < len(array):
		x = array[i]
		if x < 1:
			continue
		elif x > len(array):
			continue
		else: 
				#swap
				temp = array[x-1]
				array[x-1] = x
				array[i] = temp
		i += 1
				
				
	for i, x in enumerate(array, 1):
		if i != x:
			return i
			
	return len(array) + 1
	
	
def first_missing_positive(nums):
    if not nums:
        return 1
    for i, num in enumerate(nums):
        while i + 1 != nums[i] and 0 < num <= len(nums):
            v = nums[i]
            nums[i], nums[v - 1] = nums[v - 1], nums[i]
            if nums[i] == nums[v - 1]:
                break
    for i, num in enumerate(nums, 1):
        if num != i:
            return i
    return len(nums) + 1

	
print(first_missing_positive([5,4, 3, -2, 1,2]))

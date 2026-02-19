def moveAllZeros(nums):
    index = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index], nums[i] =nums[i], nums[index]
            index += 1
arr = [0,1,0,2,3]
moveAllZeros(arr)
print(arr)

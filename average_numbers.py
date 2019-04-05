nums = [ 5,0,8,3,4,1,6]
runningsum = 0
for num in nums: 
    runningsum += num
average = runningsum / len(nums)
print(average)
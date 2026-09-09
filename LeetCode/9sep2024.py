# 2sum problem 
def twosum(nums,target):
    n = len(nums)
    # index the array num 
    #e.g index : 0,1,2,3,4,5,6
    for i in range(n):
        #e.g index: i means current index, if 0 + 1 =1 
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
                return [ i , j]
    return []
# 26. Remove Duplicates from Sorted Array.py



class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # check empty arr
        if not nums:
            return 0
        # curr postition
        insert_pos = 1

        for i in range(1,len(nums)):

            if nums[i] != nums[i-1]:
                nums[insert_pos] = nums[i]
                # increase pos by 1 after checking once
                insert_pos +=1
            
        return insert_pos
        
        
        
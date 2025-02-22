class Solution(object):
    def missingNumber(self, nums):
      
        n = len(nums)
        
        for i in range(n):
            n = n+(i - nums[i])
        return n
            

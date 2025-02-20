class Solution(object):
    def missingNumber(self, nums):
       
        n = len(nums)
        a = 0
        for i in range(n + 1):
            a = a^i
            print a
        b = 0
        for num in nums:
            b = b ^ num
            print b
        return a ^ b
            

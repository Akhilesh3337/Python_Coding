class Solution:
    def missingNumber(self, nums):
        nums=sorted(nums)
        for i in range(len(nums)):
            if(nums[i]!=i):
                return i
        return len(nums)
    
nums=[3,0,1]
sol = Solution()
print(sol.missingNumber(nums))

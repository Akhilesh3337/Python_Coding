class Solution:
    def containsDuplicate(self, nums):
    
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            s.add(nums[i])
        return False
    
solution=Solution()
print(solution.containsDuplicate([1,2,3,4,5,6,7,8,9,10,1]))


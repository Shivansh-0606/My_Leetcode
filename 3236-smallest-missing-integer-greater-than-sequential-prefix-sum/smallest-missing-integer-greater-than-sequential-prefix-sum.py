class Solution:
    def missingInteger(self, nums: List[int]) -> int:

        j = 1
        count = 0

        while j < len(nums) and nums[j] == nums[j-1] + 1:
            
            count+=nums[j-1]
            j+=1
        
        count+=nums[j-1]

        if count not in nums:
            return count
        else:
            while count in nums:
                count+=1
            return count
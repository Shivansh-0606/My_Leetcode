class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        best = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                curr+=1
                best = max(curr,best)
            else:
                curr = 0

        return best
            
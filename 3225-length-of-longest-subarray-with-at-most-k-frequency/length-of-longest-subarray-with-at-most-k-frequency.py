class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        visited = {}

        left = 0
        max_len = 0
        
        for right in range(len(nums)):
            if nums[right] in visited:
                visited[nums[right]]+=1
            else:
                visited[nums[right]] = 1

            while visited[nums[right]] > k:
                visited[nums[left]]-=1
                left+=1

            curr_len = right - left + 1

            if curr_len > max_len:
                max_len = curr_len
        
        return max_len
            

             







class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def generate_subsets(start , curr_subset):
            res.append(list(curr_subset))

            for i in range(start , len(nums)):

                if i > start and nums[i] == nums[i-1]:
                    continue
            
                curr_subset.append(nums[i])

                generate_subsets(i+1 , curr_subset)

                curr_subset.pop()
        
        generate_subsets(0 , [])

        return res




            

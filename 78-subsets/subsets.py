class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def generate_subset(start , curr_subset):
            res.append(list(curr_subset))

            for i in range(start , len(nums)):
                curr_subset.append(nums[i])

                generate_subset(i+1 , curr_subset)

                curr_subset.pop()
        
        generate_subset(0,[])

        return res
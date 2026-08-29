class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0

        L = max(nums).bit_length()

        for i in range(L-1 , -1, -1):
            mask |= (1<<i)

            prefixes = {num & mask for num in nums}

            candidate = max_xor | (1<<i)

            for p in prefixes:
                if (p ^ candidate) in prefixes:
                    max_xor = candidate
                    break
        
        return max_xor
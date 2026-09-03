class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        def merge_sort(left: int, right: int) -> int:
            if left >= right:
                return 0
            
            mid = (left + right) // 2
            count = merge_sort(left, mid) + merge_sort(mid + 1, right)
            
            # Count reverse pairs across the two sorted halves
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and nums[i] > 2 * nums[j]:
                    j += 1
                count += j - (mid + 1)
            
            # Standard merge step
            merged = []
            p1, p2 = left, mid + 1
            while p1 <= mid and p2 <= right:
                if nums[p1] <= nums[p2]:
                    merged.append(nums[p1])
                    p1 += 1
                else:
                    merged.append(nums[p2])
                    p2 += 1
            
            while p1 <= mid:
                merged.append(nums[p1])
                p1 += 1
            while p2 <= right:
                merged.append(nums[p2])
                p2 += 1
                
            nums[left:right + 1] = merged
            return count

        return merge_sort(0, len(nums) - 1)
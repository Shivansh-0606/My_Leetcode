# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        low = 0
        high = len(nums) - 1
        mid = (low + high) // 2

        root = TreeNode()

        root.val = nums[mid]

        left = self.sortedArrayToBST(nums[:mid])

        right = self.sortedArrayToBST(nums[mid+1:])

        root.left = left
        root.right = right

        return root
         
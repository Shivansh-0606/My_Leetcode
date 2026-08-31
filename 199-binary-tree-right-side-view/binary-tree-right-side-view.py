# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def dfs(node:Optional[TreeNode] , depth:int):
            if not node:
                return 
            
            # First time visiting this depth -> must be the rightmost node
            if depth == len(res):
                res.append(node.val)
            
            #priortize right-subtree
            dfs(node.right , depth+1)
            dfs(node.left , depth+1)

        dfs(root , 0)
        return res
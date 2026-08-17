# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        
        in_idx_map = {val:idx for idx , val in enumerate(inorder)}

        def build(in_start:int ,in_end:int , post_start:int, post_end:int ) -> Optional[TreeNode]:
            if in_start > in_end or post_start > post_end:
                return None

            root_val = postorder[post_end]

            root = TreeNode(root_val)

            root_idx = in_idx_map[root_val]

            left_subtree_size = root_idx - in_start

            root.left = build(in_start ,root_idx-1, post_start, post_start + left_subtree_size -1)

            root.right = build(root_idx+1 , in_end , post_start + left_subtree_size , post_end-1 )

            return root
        
        return build(0,len(inorder)-1 , 0 , len(postorder)-1)
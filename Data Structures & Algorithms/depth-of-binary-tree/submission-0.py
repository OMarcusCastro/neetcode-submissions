
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=, Self0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,root:Optional[TreeNode],level=0,max_level=0):
        if root is None:
            return max(level,max_level)
            
        
        max_level=self.dfs(root.left,level+1,max_level)
        max_level = self.dfs(root.right,level+1,max_level)

        return max_level
        



    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
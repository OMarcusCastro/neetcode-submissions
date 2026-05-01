
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
        
    def dfs_2(self,root):
        stack = []
        max_d = 0
        if root:
            stack.append(root)
        level =0
        while len(stack)>0:

            for i in range(len(stack)):
                curr = stack.pop()

                if curr.right:
                    stack.append(curr.right)
                if curr.left:
                    stack.append(curr.left)
                level+=1
                max_d = max(level,max_d)
        return max_d
            


    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        
        def measureHeight(root):
            if root is None:
                return 0
            
            left = measureHeight(root.left)
            right = measureHeight(root.right)

            if abs(left-right)>1:
                self.ans =False
                
            return max(left,right)+1

        measureHeight(root)
        return self.ans


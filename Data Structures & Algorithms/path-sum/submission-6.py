# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, right=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def backtracking(root,sum_,targetSum):
            

            if not root:
                return False

            sum_+=root.val  
        
            if not root.left and not root.right:

                return sum_==targetSum
                   
            if backtracking(root.left,sum_,targetSum):
                return True
            if backtracking(root.right,sum_,targetSum):
                return True
            return False

        return backtracking(root,0,targetSum)
        
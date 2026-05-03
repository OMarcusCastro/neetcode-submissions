# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, right=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def backtracking(self,root,path,sum_,targetSum):
        if not root:
            return False

        path.append(root.val)
        sum_+=root.val
        
       
        if not root.left and not root.right and targetSum==sum_:
            return targetSum==sum_
        if self.backtracking(root.left,path,sum_,targetSum):
            return True
        if self.backtracking(root.right,path,sum_,targetSum):
            return True

        path.pop()
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        return self.backtracking(root,[],0,targetSum)
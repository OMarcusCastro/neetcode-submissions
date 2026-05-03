# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, right=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # self.path =[]
        def backtracking(root,sum_,targetSum):
            
            # print(f"root{root.val}")
            if not root:
                return False

            # self.path.append(root.val)
            sum_+=root.val
            # print(self.path)
            
        
            if not root.left and not root.right:
                # print("passei aqui",root.val)
                if sum_==targetSum:
                    return True
                else:
                    # print("passei aqui",root.val)
                    # self.path.pop()
                    return False
            if backtracking(root.left,sum_,targetSum):
                return True
            if backtracking(root.right,sum_,targetSum):
                return True

            # self.path.pop()
            return False

        r=backtracking(root,0,targetSum)
        # print(self.path)
        return r
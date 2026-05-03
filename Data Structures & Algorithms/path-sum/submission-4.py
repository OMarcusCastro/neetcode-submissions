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
        
       
        if not root.left and not root.right:
            return targetSum==sum_
        if self.backtracking(root.left,path,sum_,targetSum):
            return True
        if self.backtracking(root.right,path,sum_,targetSum):
            return True

        path.pop()
        return False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.path =[]
        def backtracking(root,path,sum_,targetSum):
            
            print(f"root{root.val}")
            if not root:
                return False

            path.append(root.val)
            sum_+=root.val
            print(path)
            
        
            if not root.left and not root.right:
                print("passei aqui",root.val)
                if sum_==targetSum:
                    return True
                else:
                    print("passei aqui",root.val)
                    path.pop()
                    return False
            if backtracking(root.left,path,sum_,targetSum):
                return True
            if backtracking(root.right,path,sum_,targetSum):
                return True

            path.pop()
            return False

        r=self.backtracking(root,self.path,0,targetSum)
        print(self.path)
        return r
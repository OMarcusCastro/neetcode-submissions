# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    




    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #para cada no o maior caminho abaixo dele vai ser: altura da esquerda + altura
        #da direita 
        self.ans=0
        def measureHeight(root,h=0):
            if root is None:
                return 0
            
            h1=measureHeight(root.left)
            h2=measureHeight(root.right)

            self.ans = max(self.ans,h1+h2)
            
            return 1+max(h1,h2)
        measureHeight(root)
        return(self.ans)
        

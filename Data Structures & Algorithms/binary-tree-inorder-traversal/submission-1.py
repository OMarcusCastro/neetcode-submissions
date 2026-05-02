# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.lista = []
        def inorder_dfs(root,lista=[]):

            if root is None:
                return lista

            lista=inorder_dfs(root.left,lista)
            lista.append(root.val)
            inorder_dfs(root.right,lista)
        
            return lista

        return inorder_dfs(root)
        
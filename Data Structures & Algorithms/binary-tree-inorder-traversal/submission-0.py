# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.lista = []
        def inorder_dfs(root):

            if root is None:
                return None

            inorder_dfs(root.left)
            self.lista.append(root.val)
            inorder_dfs(root.right)
        
            return root.val

        inorder_dfs(root)
        return self.lista
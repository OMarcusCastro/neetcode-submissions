class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            return (n1.val == n2.val
                    and isSameTree(n1.left, n2.left)
                    and isSameTree(n1.right, n2.right))

        def dfs(node):
            if not node:
                return False
            if isSameTree(node, subRoot):
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
        
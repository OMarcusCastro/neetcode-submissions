class Solution:
    def isTheSameTree(self,root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if root is None and subRoot is None:
            return True
        if root and subRoot:
            if root.val != subRoot.val:
                return False
            return (self.isTheSameTree(root.left,subRoot.left) and
                self.isTheSameTree(root.right,subRoot.right))
        return False
                 
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if subRoot is None:
            return True
        if root is None: 
            return False

        if self.isTheSameTree(root,subRoot):
            return True
        return (self.isSubtree(root.left,subRoot) or 
        self.isSubtree(root.right,subRoot))
            
        
    
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.ans = None
        
        def dfs(root):
            if not root or self.ans is not None:
                return 
            
            dfs(root.left)
            self.count += 1
            if self.count == k:
                self.ans = root.val
                return
                
            dfs(root.right)
        
        dfs(root)
        return self.ans
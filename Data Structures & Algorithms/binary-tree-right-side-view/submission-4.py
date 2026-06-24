# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root,level,ans):
    
    if level>len(ans):
        ans.append(root.val)

    if root.right is not None:
        ans = dfs(root.right,level+1,ans)
    if root.left is not None:
        ans= dfs(root.left,level+1,ans)
    return ans

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return dfs(root,1,[])
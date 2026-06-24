# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def dfs(root,level,maxLevel,ans):
    
    
    if level>len(ans):
        ans.append(root.val)
        # return ans

    if root.right is not None:
        ans = dfs(root.right,level+1,len(ans),ans)
    if root.left is not None:
        ans= dfs(root.left,level+1,len(ans),ans)
    return ans

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return dfs(root,1,0,[])
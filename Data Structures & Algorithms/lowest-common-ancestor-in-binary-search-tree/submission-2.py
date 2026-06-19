# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def findFirst(root,minor,mapper):
    if root is None:
        return mapper

    mapper[root.val]=1
    if minor.val == root.val:
        return mapper

    if minor.val>root.val:
        mapper = findFirst(root.right,minor,mapper)
    if minor.val<root.val:
        mapper=findFirst(root.left,minor,mapper)
    return mapper

def findSecond(root,target,mapper):
    if root is None:
        return
    if target.val == root.val:
        if mapper.get(root.val)==1:
            return root
    if target.val>root.val:
        a = findSecond(root.right,target,mapper)
        if a is not None:
            return a
    if target.val<root.val:
        b = findSecond(root.left,target,mapper)
        if b is not None:
            return b
    if mapper.get(root.val)==1:
        return root
    

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        mapper = {}
        if p.val<q.val:
            minor = p
            target =q
        else:
            minor=q
            target = p

        findFirst(root,minor,mapper)
        
        return findSecond(root,target,mapper)
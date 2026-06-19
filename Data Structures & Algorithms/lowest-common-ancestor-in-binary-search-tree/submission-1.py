# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# ans =None
# def getAns(root,p,q,count,mapper):
#     if root is None:
#         return 0
#     if root.val == p.val or root.val == q.val:
#         count+=1
#     if count==0:
#         mapper[root.val]= 1
#     if count == 2:
#         return 1
        
        
#     if getAns(root.left,p,q,count,mapper) ==1:
#         if mapper.get(root.left)==1:
#             ans = root
#         return 0
#     if getAns(root.right,p,q,count,mapper) ==1:
#         if mapper.get(root.right)==1:
#             ans = root
#         return 0

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
        
   
        # print(findSecond(root,target,mapper).val)
        return findSecond(root,target,mapper)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack1 =[]
        stack2 = []

        if p is None or q is None:
            return p == q
            

        if p.val!=q.val:
            return False
        

        stack1.append(p)
        stack2.append(q)
        

        while len(stack1):
            for i in range(len(stack1)):
                curr1 = stack1.pop()
                curr2 = stack2.pop()
                print(curr1.val,curr2.val)

                if curr1.val!=curr2.val:
                    return False
                
                if curr1.right:
                    stack1.append(curr1.right)
                    if curr2.right:
                        stack2.append(curr2.right)
                    else:
                        return False
                else:
                    if curr2.right is not None:
                        return False
                
                if curr1.left:
                    stack1.append(curr1.left)
                    if curr2.left:
                        stack2.append(curr2.left)
                    else:
                        return False
                else:
                    if curr2.left is not None:
                        return False
        return True
            
                    

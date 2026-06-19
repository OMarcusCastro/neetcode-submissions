def deleteElement(root,key):
    if root is None:
        return None
    if key == root.val:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left

        curr = root.right
        while curr.left:
            curr = curr.left
        curr.left=root.left
        res = root.right
        return res
        
    elif key < root.val:
        root.left = deleteElement(root.left,key)
    elif key > root.val:
        root.right = deleteElement(root.right,key)
    return root
    

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return deleteElement(root,key)
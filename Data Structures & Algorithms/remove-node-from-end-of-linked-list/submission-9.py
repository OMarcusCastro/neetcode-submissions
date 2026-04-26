# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getListSize(self,head:ListNode)-> int:
        size = 1
        while head.next:
            head = head.next
            size+=1
        return size
    
    def findNthNode(self,head: ListNode,nth:int)->Optional[ListNode]:
        if nth<0:
            return None
        n = 1
        while head:
            if n == nth:
                return head
            head = head.next
            n+=1
        return None
            


    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #get size
        dummy = ListNode()
        dummy.next = head
        size = self.getListSize(dummy)
        print(size)
        if size ==2:
            return None
        target= self.findNthNode(dummy,size-n)
        if size-n==1:
            head =head.next
            return head
        print("target",target.val)
        
        if target.next:
            target.next=target.next.next
        else:
            target.next=None

        return head
        #find n-k and link with node (n-k+1).next

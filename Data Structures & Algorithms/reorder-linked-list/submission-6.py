# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findMiddleNode(self,head:Optional[ListNode])->Optional[ListNode]:
        if head is None:
            return None
        fast,slow = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverseList(self,head:listNode)->ListNode:
        curr=head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # print("final",prev.val,prev.next.val)
        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:
        #find middle
        middle_node = self.findMiddleNode(head)
        # print('middle',middle_node.val,middle_node.next.val)
        #reverse half
        reverse_node = self.reverseList(middle_node)
        #interpolate response bg.next,final.next
        while head.next:
            # print(head.val,reverse_node.val,middle_node.val)
            temp = head.next
            temp2 = reverse_node.next
            head.next = reverse_node
            reverse_node.next = temp
            head = temp
            reverse_node =temp2
            

            if temp ==middle_node or temp2==middle_node:
                break
        
        
        
        
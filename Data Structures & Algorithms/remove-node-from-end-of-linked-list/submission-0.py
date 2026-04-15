# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        
        def reverseLL(head):
            newHead = None
            prev = head
            while prev:
                nxt = prev.next
                prev.next = newHead
                newHead = prev
                prev = nxt
            return newHead


        newHead = reverseLL(head)
        curr = newHead
        prev =curr
        n-=1
        while n:
            prev = curr
            curr=curr.next 
            n-=1
        
        print(f"previous Node {prev.val} and current node {curr.val}")
        # we are at the node to remove
        if prev == curr:
            newHead = curr.next
        else:
            prev.next = curr.next

        head = reverseLL(newHead)
        return head
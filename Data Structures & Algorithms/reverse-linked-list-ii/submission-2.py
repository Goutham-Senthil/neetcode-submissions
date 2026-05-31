# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(val = 0,next = head)
        before_left = dummy
        r_node = dummy
        stop = False
        l_node = head
        after_right = head


        for _ in range(right):
            if _ !=left-1 and not stop:
                before_left = before_left.next
                l_node = l_node.next
            else:
                stop = True
            after_right = after_right.next
            r_node = r_node.next
        
        curr = l_node
        prev = None
        while curr!= after_right:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # untangle the wires
        before_left.next = r_node
        l_node.next = after_right
        

        return dummy.next
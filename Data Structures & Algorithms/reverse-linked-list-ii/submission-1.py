# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        l_node = head

        for _ in range(1,left):
            l_node = l_node.next
        
        # right before left 
        if left!=1:
            left_remaining_nodes = head 
            while left_remaining_nodes.next!=l_node:
                left_remaining_nodes = left_remaining_nodes.next
        

        r_node = head
        for _ in range(1,right):
            r_node = r_node.next

        # reverse linked list
        curr = l_node
        prev = None
        right_remaining_nodes = r_node.next
        while curr!=right_remaining_nodes:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt


        # find the tail
        tail = prev 
        while tail.next:
            tail = tail.next
        if left!=1:
            left_remaining_nodes.next = prev
        tail.next = right_remaining_nodes
        return prev if left == 1 else head
        

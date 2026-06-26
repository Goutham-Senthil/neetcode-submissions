# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # make a dummy node
        dummy = ListNode(0,head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev,k)
            if not kth:
                break
            nxtGroup = kth.next
            # reverse logic
            prev = kth.next
            curr = groupPrev.next
    
            while curr and curr!= nxtGroup:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            
            # update the previous group
            nxtgroupPrev = groupPrev.next
            groupPrev.next = kth
            groupPrev = nxtgroupPrev
        


        return dummy.next
        
        # infite loop until end

    # get kth node
    def getKth(self,curr,k):
        while curr and k>0:
            curr = curr.next 
            k -=1
        return curr   
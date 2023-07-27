# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # base case if only one element return null
        if head.next == None:
            return None
        
        # initialize slow and fast pointer, and prev for storing parent of slow_ptr
        slow_ptr, fast_ptr = head, head
        prev = None

        # find middle node
        while fast_ptr and fast_ptr.next:

            # save parent of slow ptr
            prev = slow_ptr

            # move slow ptr to it's neighbour
            slow_ptr = slow_ptr.next

            # move fast ptr to it's neighbour's neighbour
            fast_ptr = fast_ptr.next.next
        
        # delete middle node 
        if prev:
            prev.next = slow_ptr.next

        return head
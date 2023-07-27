# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # intialize three pointers
        curr, prev, next1 = head, None, None
        while curr:
            # save next of current because it's going to be overwritten
            next1 = curr.next

            # change next of current pointer to prev
            curr.next = prev

            # save current pointer into prev because it's going to be updated
            prev = curr

            # update curr
            curr = next1
        return prev
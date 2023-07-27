# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        # find the middle element of linked list
        slow_ptr, fast_ptr, prev = head, head, None
       
        while fast_ptr and fast_ptr.next:
            prev = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        head_2 = prev.next
        prev.next = None

        # reverse the second half of linked list
        curr, prev, next1 = head_2, None, None
        while curr:
            next1 = curr.next
            curr.next = prev
            prev = curr
            curr = next1
        
        # estimate maximum pair sum by calculating sum of linked list 1 with linked list 2
        curr1, curr2 = head, prev
        max_sum = 0
        while curr1:
            max_sum = max(max_sum, curr1.val + curr2.val)
            curr1 = curr1.next
            curr2 = curr2.next
        
        return max_sum
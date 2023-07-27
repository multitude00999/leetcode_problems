# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case if length of linked list < 3 return linked list unchanged
        if not(head) or not(head.next) or not(head.next.next):
            return head
        
        # keep two pointers: one for connecting odd elements and the other for connecting even elements 
        i = 1
        curr = head
        prev_odd, prev_even, even_head = None, None, head.next
        while curr:
            # if odd element
            if i%2:
                if prev_odd:
                    prev_odd.next = curr
                prev_odd = curr
                
            # if even element
            else:
                if prev_even:
                    prev_even.next = curr
                prev_even = curr
            curr = curr.next
            i+=1
        
        # connect last odd element to head of even elements and make the last even element's next elelment as null
        prev_even.next = None
        prev_odd.next = even_head

        return head

        
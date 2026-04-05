# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        previous = None
        current = head

        while current:
            # keep track of the next node before reversing the link
            next = current.next
            # reverse the link
            current.next = previous
            # move previous and current one step forward
            previous = current
            # move to the next node in the original list
            current = next
        # by the end, the head and tail of the list will have swapped
        return previous
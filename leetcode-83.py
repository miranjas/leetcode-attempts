# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        # while we havent reached the end, compare the current node val with the next node val
        # if they are the same, skip the next node, otherwise move to the next node
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                # otherwise, move to the next node
                current = current.next 
        return head


solution = Solution()
print(solution.deleteDuplicates([1,1,2]))
print(solution.deleteDuplicates([1,1,2,3,3]))
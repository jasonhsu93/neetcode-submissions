# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # keep a set seen that records seen nodes, for every node we visit, we travel till the last node that 
        # we havent seen, swap with the current node, keep count of the number of nodes swapped, if number == 
        # n - 1 then we reached all swaps

        while head and head.next:
            last = head
            while last.next:
                prev = last
                last = last.next
            prev.next = None
            new = head.next 
            head.next = last
            last.next = new 
            head = new 
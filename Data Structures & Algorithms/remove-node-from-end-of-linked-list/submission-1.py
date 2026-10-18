# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # find the length 
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next 


        # find the node before the node thats getting removed
        dummy = ListNode()  
        dummy.next = head
        prev = dummy
        count = 0
        while head and count < length - n - 1:
            head = head.next
            count += 1

        # return the head based one conditions
        # 1. Removing first element
        # 2. Removing an element in the middle 
        # 3. Removing the last element
        if length == n:
            return head.next
        else:
            head.next = head.next.next
            return dummy.next

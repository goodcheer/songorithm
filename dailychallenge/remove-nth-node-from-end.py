# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = prev = ListNode(0)
        cur = prev.next = head
        fast = cur
        while n:
            fast = getattr(fast, 'next')
            n -= 1
        
        while fast is not None:
            prev = cur
            cur = cur.next
            fast = fast.next
            # print("prev", prev.val, "cur:", cur.val, "fast:", fast.val)
        prev.next = cur.next
        return dummy.next

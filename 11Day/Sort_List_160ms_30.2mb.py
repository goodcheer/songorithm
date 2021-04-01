# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        tmp = []
        root = head
        while root:
            tmp.append(root.val)
            root = root.next
        tmp.sort()
        
        root = head
        for n in tmp:
            root.val = n
            root = root.next
        return head


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    https://codeburst.io/fast-and-slow-pointer-floyds-cycle-detection-algorithm-9c7a8693f491#:~:text=Usually%2C%20the%20slow%20pointer%20will,then%20there%20is%20no%20cycle.
    """
    def detectCycle(self, head: ListNode) -> ListNode:
        # If list is empty or has only one node
        # without loop
        if (head == None or head.next == None):
                return None

        slow = head
        fast = head

        # Move slow and fast 1 and 2 steps
        # ahead respectively.
        slow = slow.next
        fast = fast.next.next

        # Search for loop using slow and
        # fast pointers
        while (fast and fast.next):
            if (slow == fast):
                break

            slow = slow.next
            fast = fast.next.next

        # If loop does not exist
        if (slow != fast):
            return None

        # If loop exists. Start slow from
        # head and fast from meeting point.
        slow = head

        while (slow != fast):
            slow = slow.next
            fast = fast.next

        return slow
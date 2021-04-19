class Solution:
  """
  https://leetcode.com/problems/swap-nodes-in-pairs/discuss/486804/Python-Simple-Solution-Memory-usage-less-than-100
  
  iter     | prev  | prev.next | prev.next.next | prev.next.next.next|
  0-backup | dummy |  a <- 1   |     b <- 2     |      c <- 3        |       1, 2, 3, 4
  0-swap   | dummy |  (2) <- b |    (1) <-b     |      (3) <- c      |       2, 1, 3, 4
  ---------|-------|-----------|----------------|--------------------|
  1-backup |  1    |  a <- 3   |     b <- 4     |      c <- None     |       2, 1, 3, 4
  1-swap   |  1    |  (4) <- b |     (3) <- a   |      (None) <- c   |       2, 1, 4, 3
  """
    def swapPairs(self, head: ListNode) -> ListNode:

        dummy = prev = ListNode(0)
        prev.next = head
		
        while prev.next and prev.next.next:
            a = prev.next
            b = prev.next.next
            c = prev.next.next.next
            prev.next = b
            prev.next.next = a
            prev.next.next.next = c
            prev = prev.next.next
        return dummy.next

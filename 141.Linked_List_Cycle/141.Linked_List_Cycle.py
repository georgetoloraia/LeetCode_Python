# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        torto = head
        h = head

        while h and h.next:
            torto = torto.next
            h = h.next.next

            if torto == h:
                return True

        return False

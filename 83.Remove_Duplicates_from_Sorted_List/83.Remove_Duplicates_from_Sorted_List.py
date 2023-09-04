# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        res = head

        while res:
            while res.next and res.next.val == res.val:
                res.next = res.next.next
            res = res.next
        return head

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if not list1:  # Base case: If list1 is empty, return list2
            return list2
        if not list2:  # Base case: If list2 is empty, return list1
            return list1
        
        if list1.val <= list2.val:
            merged_head = list1
            merged_head.next = self.mergeTwoLists(list1.next, list2)  # Recursively merge the rest of list1 and list2
        else:
            merged_head = list2
            merged_head.next = self.mergeTwoLists(list1, list2.next)  # Recursively merge the rest of list1 and list2
        
        return merged_head
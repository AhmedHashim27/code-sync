# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return None

        values = []
        curr = head
        while curr:
            values.append(curr.val)
            curr = curr.next

        values.sort()

        curr = head
        for v in values:
            curr.val = v
            curr = curr.next
        return head
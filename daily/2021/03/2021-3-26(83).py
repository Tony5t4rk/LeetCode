# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre_head = ListNode(0, head)
        cur = head
        while cur and cur.next:
            pre = cur
            cur = cur.next
            while cur and cur.val == pre.val:
                cur = cur.next
            pre.next = cur
        return pre_head.next
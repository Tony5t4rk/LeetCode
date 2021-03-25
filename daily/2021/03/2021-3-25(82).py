# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        pre_head = ListNode(0, head)
        pre = pre_head
        cur = head
        while cur and cur.next:
            nxt = cur.next
            if cur.val != nxt.val:
                pre = cur
                cur = cur.next
                continue
            while nxt and nxt.val == cur.val:
                nxt = nxt.next
            pre.next = nxt
            cur = nxt
        return pre_head.next
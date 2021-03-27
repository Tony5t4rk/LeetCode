# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        pre_head = ListNode(0, head)
        cur = head
        len = 0
        while cur:
            len += 1
            cur = cur.next
        k = (len - k % len) % len
        if k == 0:
            return head
        cur = head
        tail = None
        for i in range(k):
            if i == k - 1:
                tail = cur
            cur = cur.next
        pre_head.next = cur
        while cur.next:
            cur = cur.next
        cur.next = head
        tail.next = None
        return pre_head.next
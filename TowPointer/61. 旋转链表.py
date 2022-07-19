# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return head
        dummy = ListNode(next=head)
        n = 0
        r = dummy
        while r.next is not None:
            n += 1
            r = r.next
        k = k % n
        if k == 0:
            return head
        p = dummy
        for _ in range(n - k):
            p = p.next
        r.next = head
        head = p.next
        p.next = None
        return head


# 官方答案 闭合未环
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if k == 0 or not head or not head.next:
            return head

        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1

        if (add := n - k % n) == n:
            return head

        cur.next = head
        while add:
            cur = cur.next
            add -= 1

        ret = cur.next
        cur.next = None
        return ret

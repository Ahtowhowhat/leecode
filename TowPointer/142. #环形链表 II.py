# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast is not None:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
            fast = fast.next
            if fast == slow:
                break
        if fast is None:
            return None
        p = head
        while p != slow:
            p = p.next
            slow = slow.next
        return p

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        lst = []
        p = head
        while p is not None:
            lst.append(p.val)
            p = p.next
        p = head
        i, j = 0, len(lst) - 1
        while i < j:
            if lst[i] != lst[j]:
                return False
            i += 1
            j -= 1
        return True


# 将空间复杂度降到 O(1)
# 缺点：在并发环境下，函数运行时需要锁定其他线程或进程对链表的访问，因为在函数执行过程中链表会被修改。
class Solution(object):
    def reverse_LinkList(self, head: ListNode):
        pre = None
        cur = head
        while cur:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre

    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None:
            return True
        slow = fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        reversed_second_part = self.reverse_LinkList(slow.next)
        p, q = head, reversed_second_part
        ans = True
        while q is not None:
            if q.val != p.val:
                ans = False
                break
            q = q.next
            p = p.next
        slow.next = self.reverse_LinkList(reversed_second_part)
        return ans

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# ****头插法和尾插法不能直接混用。当第一个节点用头插法插入后，rear如果不跟着跟新将会指向错误节点****
# ****修复上述bug后依然不能满足题意，因为头插法不能保证原来的相对位置****
# class Solution:
#     def partition(self, head: ListNode, x: int) -> ListNode:
#         head_node = ListNode()
#         rear = None
#         p = head
#         while p is not None:
#             node = p
#             p = p.next
#             if node.val < x:
#                 node.next = head_node.next
#                 head_node.next = node
#                 if rear is None:
#                     rear = node
#             else:
#                 rear.next = node
#                 rear = node
#         rear.next = None
#         return head_node.next

# 正解
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        head_small = ListNode()
        head_large = ListNode()
        rear_small = head_small
        rear_large = head_large
        p = head
        while p is not None:
            if p.val < x:
                rear_small.next = p
                rear_small = p
            else:
                rear_large.next = p
                rear_large = p
            p = p.next
        rear_small.next = head_large.next
        rear_large.next = None
        return head_small.next

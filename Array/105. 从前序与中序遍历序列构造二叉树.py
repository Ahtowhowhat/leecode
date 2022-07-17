# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def create(pre_left, pre_right, in_left, in_right) -> TreeNode:
            if pre_left>pre_right:
                return None
            nonlocal hashmap
            val = preorder[pre_left]
            idx_inorder = hashmap[val]
            num_left = idx_inorder - in_left
            root = TreeNode(val)
            root.left = create(pre_left + 1, pre_left + num_left, in_left, idx_inorder - 1)
            root.right = create(pre_left + num_left + 1, pre_right, idx_inorder + 1, in_right)
            return root

        n = len(preorder)
        hashmap = dict(zip(inorder, range(n)))
        return create(0, n - 1, 0, n - 1)

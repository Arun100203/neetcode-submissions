# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        ans = 0

        def inorder(root, high):
            if not root:
                return

            inorder(root.left, max(high, root.val))

            if root.val >= high:
                nonlocal ans
                ans += 1

            inorder(root.right, max(high, root.val))

        inorder(root, root.val)

        return ans
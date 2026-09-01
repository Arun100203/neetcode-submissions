# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        cur = root
        pre = None
        if not root:
            return TreeNode(val)
        while cur:

            if val < cur.val:
                pre = cur
                cur = cur.left

            else:
                pre = cur
                cur = cur.right

        # print(pre.val)
        if pre.val > val:
            pre.left = TreeNode(val)
        else:
            pre.right = TreeNode(val)

        return root
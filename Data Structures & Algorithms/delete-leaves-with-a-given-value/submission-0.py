# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        
        cur = root
        noLeafFound = True

        def isLeaf(root):
            return not (root.left or root.right)

        sta = []
        sta.append(root)
        while sta:
            cur = sta.pop()

            if cur.left and cur.left.val == target:
                if isLeaf(cur.left):
                    cur.left = None
                    noLeafFound = False

            if cur.right and cur.right.val == target:
                if isLeaf(cur.right):
                    cur.right = None
                    noLeafFound = False 

            if cur.left:
                sta.append(cur.left)
            if cur.right:
                sta.append(cur.right)

        if noLeafFound:
            if cur.val == target and isLeaf(cur):
                return None
            return root

        return self.removeLeafNodes(root, target)
            

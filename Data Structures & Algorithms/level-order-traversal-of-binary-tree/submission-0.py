# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if not root:
            return []
        sta = []
        cur = root
        res = []
        sta.append(cur)
        while sta:
            temp = []
            bu = []
            while sta:
                t = sta.pop()
                bu.append(t)
                temp.append(t.val)

            if temp:
                res.append(temp)

            while bu:
                n = bu.pop()
                
                if n.right:
                    sta.append(n.right)
                if n.left:
                    sta.append(n.left)


        return res




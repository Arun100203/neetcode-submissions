# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return []
        # res = []

        # stack = []

        # cur = root
        # stack.append(cur)

        # while stack:
        #     te = []
            
        #     cur = stack.pop()

        #     res.append(cur.val)

        #     if cur.right != None:
        #         stack.append(cur.right)

        #     if cur.left != None:
        #         stack.append(cur.left)

        def preorder(root, li):
            if root == None:
                return 

            li.append(root.val)
            preorder(root.left, li)
            preorder(root.right, li)

        li = []


        preorder(root, li)


        return li

            
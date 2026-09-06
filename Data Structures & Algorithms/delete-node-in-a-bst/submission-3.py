# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        
        cur = root

        if cur.val == key:
            return self.helper(cur)
            

        while cur:

            if cur.val > key:
                if cur.left and cur.left.val == key:
                    cur.left = self.helper(cur.left)
                    return root
                else:
                    cur = cur.left
            else:
                if cur.right and cur.right.val == key:
                    cur.right = self.helper(cur.right)
                    return root
                else:
                    cur = cur.right

        return root
        
    def helper(self, node: TreeNode) -> Optional[TreeNode]:
        # Case 1: No right child? Just promote the left side.
        if not node.right:
            return node.left
            
        # Case 2: No left child? Just promote the right side.
        if not node.left:
            return node.right
            
        # Case 3: The node has BOTH children. 
        # (This is your original clever merging logic!)
        right_tree = node.right
        left_tree = node.left
        
        # 1. Find the leftmost node of the right subtree
        leftmost = right_tree
        while leftmost.left:
            leftmost = leftmost.left
            
        # 2. Attach the orphaned left tree to that leftmost node
        leftmost.left = left_tree
        
        # 3. Return the right tree, which now acts as the new root of this section
        return right_tree


        
        

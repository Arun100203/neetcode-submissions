# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        que = deque()
        res = []
        if not root:
            return ""
        que.append(root)
        
        while que:
            last = que.popleft()
            if last:
                res.append(str(last.val))
                que.append(last.left)
                que.append(last.right)
            else:
                res.append('None')
        
        # print(" ".join(res))
        return " ".join(res)


        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        li = data.split(" ")


        i = 0 
        res = TreeNode(int(li[i]))
        ans = res
        
        que = deque()

        que.append(res)
        while que and i < len(li):
            cur = que.popleft()

            i += 1
            if i < len(li) and li[i] != 'None':
                cur.left = TreeNode(li[i])
                que.append(cur.left)

            i += 1
            if i < len(li) and li[i] != 'None':
                cur.right = TreeNode(li[i])
                que.append(cur.right)
            

        return ans

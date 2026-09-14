"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def fun(grid, start, end):
            allSame = True

            val = grid[start[0]][start[1]]
            for i in range(start[0], end[0]+1):
                for j in range(start[1], end[1]+1):
                    if grid[i][j] != val:
                        allSame = False
                        break

                if not allSame:
                    break
            return val, allSame


        ans = Node()
        r, c = len(grid), len(grid[0])

        sta = []
        sta.append((ans, (0,0), (r-1,c-1)))
        while sta:
            tup = sta.pop()

            preStart, preEnd = tup[1], tup[2]

            val, allSame = fun(grid, preStart, preEnd)


            node = tup[0]
            node.isLeaf = allSame
            node.val = bool(val)

            if not node.isLeaf:
                preStart, preEnd = tup[1], tup[2]
                row_start, col_start = preStart[0], preStart[1]
                row_end, col_end = preEnd[0], preEnd[1]
                mid_row = row_start + (row_end - row_start) // 2
                mid_col = col_col = col_start + (col_end - col_start) // 2

                node.topLeft = Node()
                node.topRight = Node()
                node.bottomLeft = Node()
                node.bottomRight = Node()
                sta.append((node.topLeft, (row_start, col_start), (mid_row, mid_col)))
                sta.append((node.topRight, (row_start, mid_col + 1), (mid_row, col_end)))
                sta.append((node.bottomLeft, (mid_row + 1, col_start), (row_end, mid_col)))
                sta.append((node.bottomRight, (mid_row + 1, mid_col + 1), (row_end, col_end)))

        return ans


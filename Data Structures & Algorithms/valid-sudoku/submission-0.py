class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        for i in range(n):
            dr = {}
            dc = {}
            for j in range(n):
                if board[i][j] != '.' and board[i][j] in dr:
                    return False
                else:
                    dr[board[i][j]] = 1

                if board[j][i] != '.' and board[j][i] in dc:
                    return False
                else:
                    dc[board[j][i]] = 1

                if i in [0, 3, 6] and j in [0, 3, 6]:
                    ds = {}
                    # print("------")
                    for k in range(i, i+3):
                        for l in  range(j, j+3):
                            # print(k, l)
                            if board[k][l] != '.' and board[k][l] in ds:
                                return False
                            else:
                                ds[board[k][l]] = 1 

        return True

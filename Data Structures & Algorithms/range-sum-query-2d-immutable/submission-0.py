class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.ma = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ma = self.ma
        cnt = 0
        for i in range(row2 - row1 + 1):
            for j in range(col2 - col1 + 1):
                cnt += (ma[row1+i][col1+j])
                # print(row1+i, col1+j)

        return cnt



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        n = len(matrix)
        m = len(matrix[0])

        for i in range(n):

            if matrix[i][0] > target:
                row = i - 1
                break
            elif matrix[i][0] == target:
                row = i
                break

        if row ==-1:
            row = n-1
        print(row)
        i = 0
        j = m-1
        while i <= j:
            
            mid = i + (j-i) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                j = mid - 1
            else:
                i = mid + 1
            
        return False

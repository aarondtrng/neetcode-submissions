class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLow = 0
        rowHigh = len(matrix)-1
        colLow = 0
        colHigh = len(matrix[0])
        while rowLow <= rowHigh and colLow <= colHigh:
            rowMid = rowLow + rowHigh // 2
            colMid = colLow + colHigh // 2
            if matrix[rowMid][colMid] == target:
                return True
            elif matrix[rowMid][colMid] > target:
                if matrix[rowMid][colLow] > target:
                    rowHigh = rowMid - 1
                    colLow = 0
                    colHigh = len(matrix[0])
                else:
                    colHigh = colMid - 1
            elif matrix[rowMid][colMid] < target:
                if matrix[rowMid][colLow] > target:
                    rowLow = rowMid + 1
                    colLow = 0
                    colHigh = len(matrix[0])
                else:
                    colLow = colMid + 1
        return False
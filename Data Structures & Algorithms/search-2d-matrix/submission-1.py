class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rowLow = 0
        rowHigh = len(matrix)-1
        while rowLow <= rowHigh:
            rowMid = (rowLow + rowHigh) // 2
            if matrix[rowMid][0] <= target <= matrix[rowMid][-1]:
                break;
            elif matrix[rowMid][0] > target:
                rowHigh = rowMid - 1
            elif matrix[rowMid][len(matrix[0])-1] < target:
                rowLow = rowMid + 1
        
        low = 0
        high = len(matrix[0])-1
        while low <= high:
            mid = (low + high)// 2
            if matrix[rowMid][mid] == target:
                return True
            elif matrix[rowMid][mid] < target:
                low = mid+1
            elif matrix[rowMid][mid] > target: 
                high = mid-1
        return False
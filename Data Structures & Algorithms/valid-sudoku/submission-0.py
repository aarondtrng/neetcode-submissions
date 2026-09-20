class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:        
        for row in board:
            filter = [num for num in row if num != "."]
            if len(set(filter)) != len(filter):
                return False
        for c in range(9):
            col = [board[r][c] for r in range(9) if board[r][c] != "."]
            if len(set(col)) != len(col):
                return False

        boxes = {}
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                index = (r//3) * 3 + (c//3)
                if index not in boxes:
                    boxes[index] = []
                boxes[index].append(board[r][c])

        for vals in boxes.values():
            if len(set(vals)) != len(vals):
                return False
        return True

            
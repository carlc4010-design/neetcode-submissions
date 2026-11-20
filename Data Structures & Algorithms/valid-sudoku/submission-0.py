class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #---
        n = len(board)
        for i in range(n):
            myMap = {}
            for j in range(n):
                if board[i][j] in ("1","2","3","4","5","6","7","8","9") :
                    if board[i][j] in myMap:
                        return False
                    else:
                        myMap[board[i][j]] = board[i][j]
        for j in range(n):
            myMap = {}
            for i in range(n):
                if board[i][j] in ("1","2","3","4","5","6","7","8","9") :
                    if board[i][j] in myMap:
                        return False
                    else:
                        myMap[board[i][j]] = board[i][j]
        for u in range(3):
            for v in range(3):
                myMap= {}
                for i in range(3):
                    for j in range(3):
                        if board[i+u*3][j+v*3] in ("1","2","3","4","5","6","7","8","9") :
                            if board[i+u*3][j+v*3] in myMap:
                                return False
                            else:
                                myMap[board[i+u*3][j+v*3]] = board[i+u*3][j+v*3]
        return True
                
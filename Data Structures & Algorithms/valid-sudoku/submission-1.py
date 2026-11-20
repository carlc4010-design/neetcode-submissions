class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowD = defaultdict(set) 
        colD = defaultdict(set)
        sqD  = defaultdict(set)

        for i in range(9):
            for j in range(9):
                val =  board[i][j]
                if val == ".":
                    continue
                if val in rowD[i]:
                    return False
                else:
                    rowD[i].add(val)
                if val in colD[j]:
                    return False
                else:
                    colD[j].add(val)
                if val in sqD[(i//3, j//3)]:
                    return False
                else:
                    sqD[(i//3,j//3)].add(val)
                
        return True  
                 
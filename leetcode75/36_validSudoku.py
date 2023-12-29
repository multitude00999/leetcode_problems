class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n, m = len(board), len(board[0])

        # check rows
        for i in range(n):
            temp = set()
            for j in range(m):
                if board[i][j]!= '.' and board[i][j] in temp:
                    return False
                if board[i][j]!= '.':
                    temp.add(board[i][j])
        
        # check cols
        for j in range(m):
            temp = set()
            for i in range(n):
                if board[i][j]!= '.' and board[i][j] in temp:
                    return False
                if board[i][j]!= '.':
                    temp.add(board[i][j])

        # check 3x3 squares
        for i in range(0, n, 3):
            for j in range(0, m,3):
                temp = set()
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        if board[k][l]!= '.' and board[k][l] in temp:
                            return False
                        if board[k][l]!= '.':
                            temp.add(board[k][l])

        return True
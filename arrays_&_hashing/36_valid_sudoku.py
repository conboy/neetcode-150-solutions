class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check rows for dupe
        for row in board:
            seen = set()
            for num in row:
                if num in seen:
                    return False
                if num != '.':
                    seen.add(num)
        # check column for dupe
        for i in range(len(board)):
            seen = set()
            for j in range(len(board)):
                if board[j][i] in seen:
                    return False
                if board[j][i] != '.':
                    seen.add(board[j][i])

        # check squares for dupe
        for i in range(1, len(board), 3):
            for j in range(1, len(board), 3):
                seen = set()
                for l in range(-1, 2, 1):
                    for k in range(-1, 2, 1):
                        num = board[i+k][j+l]
                        # print(board[i+k][j+l])
                        if num in seen:
                            return False
                        if num != '.':
                            seen.add(num)

        return True
def queen_problem(n):
    board = [-1]*n

    def is_safe(row,col):
        for i in range(row):
            c = board[i]
            if c == col or abs(c-col) == abs(i-row):
                return False
        return True

    def backtrack(row):
        if row == n:
            print_board()
            return True

        for col in range(n):
            if is_safe(row,col):
                board[row] = col
                if backtrack(row+1):
                    return True
                board[row] = -1
        return False

    def print_board():
        for i in range(n):
            line = ['Q' if c == board[i] else '-' for c in range(n)]
            print(' '.join(line))
        print()

    if not backtrack(0):
        print("No solution")

queen_problem(8)

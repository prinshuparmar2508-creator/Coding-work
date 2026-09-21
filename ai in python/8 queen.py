def solve_n_queens(n=8):
    board = [-1] * n  # board[i] = column of queen in row i

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            print_board()
            return True  # remove this line + return to find ALL solutions
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                if backtrack(row + 1):
                    return True
                board[row] = -1
        return False

    def print_board():
        for r in range(n):
            line = ['Q' if c == board[r] else '.' for c in range(n)]
            print(' '.join(line))
        print()

    if not backtrack(0):
        print("No solution")

solve_n_queens(8)
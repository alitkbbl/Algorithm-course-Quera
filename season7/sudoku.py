def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end=" ")
        print()


def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


def is_valid(board, num, pos):
    row, col = pos

    for j in range(9):
        if board[row][j] == num and j != col:
            return False

    for i in range(9):
        if board[i][col] == num and i != row:
            return False

    box_row = row // 3
    box_col = col // 3

    for i in range(box_row * 3, box_row * 3 + 3):
        for j in range(box_col * 3, box_col * 3 + 3):
            if board[i][j] == num and (i, j) != (row, col):
                return False

    return True


def solve_sudoku(board):
    empty = find_empty(board)

    if not empty:
        return True

    row, col = empty

    for num in range(1, 10):
        if is_valid(board, num, (row, col)):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            board[row][col] = 0

    return False


def main():
    board = []
    for _ in range(9):
        row = list(map(int, input().split()))
        board.append(row)


    if solve_sudoku(board):
        print_board(board)
    else:
        print("No solution exists")


if __name__ == "__main__":
    main()
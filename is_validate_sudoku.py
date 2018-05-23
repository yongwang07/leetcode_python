def is_valid_sudoku(board):
    row_flag = [set() for _ in range(len(board))]
    col_flag = [set() for _ in range(len(board))]
    cell_flag = [set() for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == '.':
                continue
            if board[i][j] in row_flag[i]:
                return False
            row_flag[i].add(board[i][j])
            if board[i][j] in col_flag[j]:
                return False
            col_flag[j].add(board[i][j])
            cell_idx = (i // 3) * 3 + (j // 3)
            if board[i][j] in cell_flag[cell_idx]:
                return False
            cell_flag[cell_idx].add(board[i][j])
    return True


if __name__ == '__main__':
    print('leetcode 36')
    board = [['5', '3', '.', '.', '7', '.', '.', '.', '.'],
             ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
             ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
             ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
             ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
             ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
             ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
             ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
             ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    print(is_valid_sudoku(board))
    board = [['8', '3', '.', '.', '7', '.', '.', '.', '.'],
         ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
         ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
         ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
         ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
         ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
         ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
         ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
         ['.', '.', '.', '.', '8', '.', '.', '7', '9']]
    print(is_valid_sudoku(board))


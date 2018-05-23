INF = 2147483647


def helper(grid, i, j, level):
    if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0 or grid[i][j] < level:
        return
    grid[i][j] = level
    helper(grid, i + 1, j, level + 1)
    helper(grid, i - 1, j, level + 1)
    helper(grid, i, j + 1, level + 1)
    helper(grid, i, j - 1, level + 1)


def wall_and_gate(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                helper(grid, i, j, 0)
    return grid


def game_life(board):
    m, n = len(board), len(board[0])
    dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
    for i in range(m):
        for j in range(n):
            count = 0
            for x, y in dirs:
                new_x, new_y = i + x, j + y
                if 0 <= new_x < m and 0 <= new_y < n and (board[new_x][new_y] == 1 or board[new_x][new_y] == 2):
                    count += 1
            if (count < 2 or count > 3) and board[i][j] == 1:
                board[i][j] = 2
            elif count == 3 and board[i][j] == 0:
                board[i][j] = 3
    for i in range(m):
        for j in range(n):
            board[i][j] %= 2


def word_pattern(pattern, str):
    words = str.split(' ')
    if len(pattern) != len(words):
        return False
    p2w, w2p = dict(), dict()
    for i in range(len(pattern)):
        if pattern[i] not in p2w and words[i] not in w2p:
            p2w[pattern[i]] = words[i]
            w2p[words[i]] = pattern[i]
        elif p2w.get(pattern[i], None) != words[i] or w2p.get(words[i], None) != pattern[i]:
            return False
    return True


if __name__ == '__main__':
    print('leetcode 286, 289, 290')
    print(wall_and_gate([[INF, -1, 0, INF], [INF, INF, INF, -1],
                   [INF,  -1, INF, -1], [0, -1, INF, INF]]))
    board = [[1, 0, 1, 1], [0, 1, 1, 0], [1, 0, 1, 0], [0, 0, 0, 1]]
    game_life(board)
    print(board)
    print(word_pattern('abba', 'dog cat cat dog'))
    print(word_pattern('abba', 'dog cat cat fish'))
    print(word_pattern('aaaa', 'dog cat cat dog'))
    print(word_pattern('abba', 'dog dog dog dog'))

def search(matrix, word, start, i, j, visited):
    if start == len(word):
        return True
    if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]) or visited[i][j] or matrix[i][j] != word[start]:
        return False
    visited[i][j] = True
    res = search(matrix, word, start + 1, i + 1, j, visited) or \
        search(matrix, word, start + 1, i - 1, j, visited) or \
        search(matrix, word, start + 1, i, j - 1, visited) or \
        search(matrix, word, start + 1, i, j + 1, visited)
    visited[i][j] = False
    return res


def word_search(matrix, word):
    row, col = len(matrix), len(matrix[0])
    visited = [[False for _ in range(col)] for _ in range(row)]
    for i in range(row):
        for j in range(col):
            if search(matrix, word, 0, i, j, visited):
                return True
    return False


if __name__ == '__main__':
    print('leetcode 79')
    print(word_search([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED'))
    print(word_search([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE'))
    print(word_search([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB'))



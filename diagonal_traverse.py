def diagonal_traverse(matrix):
    m, n, res = len(matrix), len(matrix[0]), []
    for i in range(m + n):
        low = max(0, i - n + 1)
        high = min(i, m - 1)
        if i % 2 == 0:
            for k in range(high, low - 1, -1):
                res.append(matrix[k][i - k])
        else:
            for k in range(low, high + 1):
                res.append(matrix[k][i - k])
    return res

if __name__ == '__main__':
    print('leetcode 498')
    print(diagonal_traverse([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

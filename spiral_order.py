def spiral_order(matrix):
    ret = []
    left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            ret.append(matrix[top][i])
        top += 1
        for j in range(top, bottom + 1):
                ret.append(matrix[j][right])
        right -= 1
        if top <= bottom:
            for m in range(right, left - 1, -1):
                ret.append(matrix[bottom][m])
        bottom -= 1
        for n in range(bottom, top - 1, -1):
            ret.append(matrix[n][left])
        left += 1
    return ret


def can_jump(steps):
    reach = 0
    for i, n in enumerate(steps):
        if i > reach:
            return False
        reach = max(reach, i + n)
    return True

def generate_matrix(n):
    res = [[0 for _ in range(n)] for _ in range(n)]
    val, p = 1, n
    for i in range(n//2):
        for col in range(i, i + p):
            res[i][col] = val
            val += 1
        for row in range(i + 1, i + p):
            res[row][i + p - 1] = val
            val += 1
        for col in range(i + p - 2, i - 1, -1):
            res[i + p - 1][col] = val
            val += 1
        for row in range(i + p - 2, i, -1):
            res[row][i] = val
            val += 1
        i += 1
        p -= 2
    if n % 2 != 0:
        res[n // 2][n // 2] = val
    return res


if __name__ == '__main__':
    print('leetcode 54, 55, 59')
    print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(spiral_order([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]))
    print(spiral_order([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]))
    print(can_jump([2, 3, 1, 1, 4]))
    print(can_jump([3, 2, 1, 0, 4]))
    print(generate_matrix(3))

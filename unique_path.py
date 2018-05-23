def unique_path(m, n):
    dp = [1 for _ in range(n)]
    for row in range(1, m):
        for col in range(1, n):
            dp[col] += dp[col - 1]
    return dp[n - 1]


def unique_path_in_obstacle(obstacle):
    m, n = len(obstacle), len(obstacle[0])
    dp = [0 for _ in range(n)]
    dp[0] = 1
    for row in range(m):
        for col in range(n):
            if obstacle[row][col] == 1:
                dp[col] = 0
            elif col > 0:
                dp[col] += dp[col - 1]
    return dp[n - 1]


def min_path_sum(matrix):
    m, n = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(n)] for _ in range(2)]
    print(dp)
    for row in range(m):
        for col in range(n):
            if row == 0:
                dp[row % 2][col] = (dp[row % 2][col - 1] if col > 0 else 0) + matrix[row][col]
            elif col == 0:
                dp[row % 2][col] = (dp[(row - 1) % 2][col] if row > 0 else 0) + matrix[row][col]
            else:
                dp[row % 2][col] = min(dp[row % 2][col - 1], dp[(row - 1) % 2][col]) + matrix[row][col]
    return dp[(m - 1) % 2][n - 1]


if __name__ == '__main__':
    print('leetcode 62, 63')
    print(unique_path(3, 7))
    print(unique_path_in_obstacle([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
    print(min_path_sum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))

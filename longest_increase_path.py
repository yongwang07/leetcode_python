from collections import deque


def longest_increase_path(matrix):
    m, n, res, m_x, m_y = len(matrix), len(matrix[0]), 1, 0, 0
    dp = [[0] * n for _ in range(m)]
    dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
    for i in range(m):
        for j in range(n):
            if dp[i][j] > 0:
                continue
            q, count = deque(), 1
            q.append((i, j))
            while len(q) > 0:
                size = len(q)
                count += 1
                for _ in range(size):
                    cur_x, cur_y = q.popleft()
                    for x, y in dirs:
                        nx, ny = x + cur_x, y + cur_y
                        if nx < 0 or nx >= m or ny < 0 or ny >= n or matrix[cur_x][cur_y] >= matrix[nx][ny] or \
                                count <= dp[nx][ny]:
                            continue
                        dp[nx][ny] = count
                        if res < count:
                            res = count
                            m_x, m_y = nx, ny
                        q.append((nx, ny))
    path = []
    while res > 0:
        path.append(matrix[m_x][m_y])
        res -= 1
        for dx, dy in dirs:
            x, y = dx + m_x, dy + m_y
            if x < 0 or x >= m or y < 0 or y >= n or dp[x][y] != dp[m_x][m_y] - 1:
                continue
            break
        m_x, m_y = x, y
    return path


if __name__ == '__main__':
    print('leetcode 329')
    print(longest_increase_path([[3, 4, 5], [3, 2, 6], [2, 2, 1]]))
    print(longest_increase_path([[9, 9, 4], [6, 6, 8], [2, 1, 1]]))
    print('LGB' < 'LGA')

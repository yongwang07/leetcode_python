from copy import copy
from collections import deque


def helper(n, start, k, tmp, res):
    if n - start + 1 < k:
        return
    if k == 0:
        res.append(copy(tmp))
        return
    for i in range(start, n + 1):
        tmp.append(i)
        helper(n, i + 1, k - 1, tmp, res)
        tmp.pop()


def combine(n, k):
    tmp, res = [], []
    helper(n, 1, k, tmp, res)
    return res


def combine_2(n, k):
    q = deque([[i] for i in range(1, n + 1)])
    k -= 1
    for _ in range(k):
        for _ in range(len(q)):
            cur = q.popleft()
            for i in range(cur[-1] + 1, n + 1):
                q.append(cur + [i])
    return list(q)


if __name__ == '__main__':
    print('leetcode 77')
    print(combine(5, 3))
    print(combine_2(5, 3))

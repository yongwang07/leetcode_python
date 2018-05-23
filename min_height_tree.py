from collections import deque, defaultdict


def min_height_tree(n, edges):
    d = defaultdict(set)
    for a, b in edges:
        d[a].add(b)
        d[b].add(a)
    q = deque()
    for i in range(n):
        if len(d[i]) == 1:
            q.append(i)
    while n > 2:
        size = len(q)
        n -= size
        for _ in range(size):
            t = q.popleft()
            for x in d[t]:
                d[x].remove(t)
                if len(d[x]) == 1:
                    q.append(x)
    return list(q)


def can_schedule(n, edges):
    _out = defaultdict(set)
    _in = defaultdict(int)
    for a, b in edges:
        _in[b] += 1
        _out[a].add(b)
    q = deque()
    visited = set()
    for i in range(n):
        if _in[i] == 0:
            q.append(i)
    while len(q) > 0:
        cur = q.popleft()
        if cur in visited:
            return False
        visited.add(cur)
        for neigh in _out[cur]:
            _in[neigh] -= 1
            if _in[neigh] == 0:
                q.append(neigh)
    return len(visited) == n


def find_order(n, edges):
    _out = defaultdict(set)
    _in = defaultdict(int)
    for a, b in edges:
        _in[b] += 1
        _out[a].add(b)
    q = deque()
    res = []
    for i in range(n):
        if _in[i] == 0:
            q.append(i)
    while len(q) > 0:
        cur = q.popleft()
        res.append(cur)
        for neigh in _out[cur]:
            _in[neigh] -= 1
            if _in[neigh] == 0:
                q.append(neigh)
    res.reverse()
    return res


if __name__ == '__main__':
    print('leetcode 310, 207, 210')
    print(min_height_tree(4, [[1, 0], [1, 2], [1, 3]]))
    print(min_height_tree(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))
    print(can_schedule(2, [[1, 0]]))
    print(can_schedule(2, [[1, 0], [0, 1]]))
    print(find_order(2, [[1, 0]]))
    print(find_order(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))


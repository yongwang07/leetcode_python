from collections import defaultdict


def connect_component(n, edges):
    def dfs(cur):
        if cur in visited:
            return
        visited.add(cur)
        for neighbor in m[cur]:
            dfs(neighbor)

    visited = set()
    m = defaultdict(list)
    for start, to in edges:
        m[start].append(to)
        m[to].append(start)
    res = 0
    for i in range(n):
        if i not in visited:
            res += 1
            dfs(i)
    return res


def connect_component_2(n, edges):
    def find_root(i):
        while root[i] != i:
            i = root[i]
        return i
    res = n
    root = [i for i in range(n)]
    for start, end in edges:
        r1, r2 = find_root(start), find_root(end)
        if r1 != r2:
            res -= 1
            root[r2] = r1
    return res


if __name__ == '__main__':
    print('leetcode 323')
    print(connect_component(5, [[0, 1], [1, 2], [3, 4]]))
    print(connect_component(5,  [[0, 1], [1, 2], [2, 3], [3, 4]]))
    print(connect_component_2(5, [[0, 1], [1, 2], [3, 4]]))
    print(connect_component_2(5,  [[0, 1], [1, 2], [2, 3], [3, 4]]))

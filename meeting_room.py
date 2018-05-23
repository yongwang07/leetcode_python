from collections import defaultdict, OrderedDict, deque, Counter
from functools import cmp_to_key


def meeting_room(arr):
    d = defaultdict(int)
    for start, end in arr:
        d[start] += 1
        d[end] -= 1

    def comp(a, b):
        if a[1] != b[1]:
            return a[1] - b[1]
        else:
            return a[0] - b[0]
    dict(sorted(d.items(), key=cmp_to_key(comp)))
    sorted_map = OrderedDict(sorted(d.items()))
    res, min_room = 0, 0
    for value in sorted_map.values():
        res += value
        min_room = max(min_room, res)
    return min_room


def valid_tree(n, edges):
    s, q, g = set(), deque([0]), [set() for _ in range(n)]
    for start, end in edges:
        g[start].add(end)
    while len(q) > 0:
        cur = q.pop()
        if cur in s:
            return False
        s.add(cur)
        for a in g[cur]:
            q.append(a)
    return len(s) == n


def helper(tmp, start, end, res, d):
    if start >= end:
        res.append(''.join(tmp))
        return
    for key, values in d.items():
        if values > 1:
            tmp[start] = key
            tmp[end] = key
            d[key] -= 2
            helper(tmp, start + 1, end - 1, res, d)
            d[key] += 2


def generate_palindromes(s):
    d = Counter(s)
    odds = [key for key , values in d.items() if values == 1]
    if len(odds) > 1 or len(odds) != len(s) % 2:
        return []
    tmp = [None for _ in range(len(s))]
    res = []
    if len(s) % 2 == 1:
        tmp[len(s)//2] = odds[0]
        d.pop(odds[0])
    helper(tmp, 0, len(s) - 1, res, d)
    return res


def decode(s):
    k, str_st, num_st = 0, [], []
    for c in s:
        if c.isdigit():
            k = 10 * k + int(c)
        elif c == '[':
            num_st.append(k)
            k = 0
            str_st.append(c)
        elif c.isalpha():
            str_st.append(c)
        elif c == ']':
            tmp = ''
            while len(str_st) > 0 and str_st[-1] != '[':
                tmp = str_st.pop() + tmp
            str_st.pop()
            tmp = tmp * num_st.pop()
            str_st.append(tmp)
    return ''.join(str_st)


if __name__ == '__main__':
    print('leetcode 253, 261, 267, 271, 394')
    print(meeting_room([[0, 30], [5, 10], [15, 20]]))
    print(valid_tree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
    print(valid_tree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
    print(generate_palindromes('aabbbbcc'))
    print(generate_palindromes('abc'))
    print(decode('3[a]2[bc]'))
    print(decode('3[a2[c]]'))
    print(decode('2[abc]3[cd]ef'))


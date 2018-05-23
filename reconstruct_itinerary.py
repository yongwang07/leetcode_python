from collections import defaultdict, Counter


def reconstruct_itinerary(tickets):
    d = defaultdict(list)
    for start, to in sorted(tickets, reverse=True):
        d[start].append(to)
    cur, res = 'JFK', ['JFK']
    while len(d) > 0:
        res.append(d[cur].pop())
        if len(d[cur]) == 0:
            d.pop(cur)
        cur = res[-1]
    return res


def depth_sum(nested_list):
    def dfs(sub, depth):
        s = 0
        for i in sub:
            s += depth * i if type(i) is int else dfs(i, depth + 1)
        return s
    return dfs(nested_list, 1)


def depth_sum_2(nested_list):
    res = [0]

    def helper(sub, depth):
        nonlocal res
        if len(res) < depth + 1:
            res += [0] * (depth - len(res) + 1)
        for j in sub:
            if type(j) is int:
                res[depth] += j
            else:
                helper(j, depth + 1)
    helper(nested_list, 0)
    total = 0
    for i in range(len(res)):
        total += res[i] * (len(res) - i)
    return total


def nested_iterator(nested_list):
    for i in nested_list:
        if type(i) is int:
            yield i
        else:
            yield from nested_iterator(i)


def reverse_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    s = list(s)
    i, j = 0, len(s) - 1
    while i < j:
        if s[i] not in vowels:
            i += 1
        if s[j] not in vowels:
            j -= 1
        if s[i] in vowels and s[j] in vowels:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1
    return ''.join(s)


def top_k_freq(nums, k):
    counter = Counter(nums)
    r = sorted(counter.items(), key=lambda item: item[1], reverse=True)
    res, i = [], 0
    while i < k:
        res.append(r[i][0])
        i += 1
    return res


def top_k_freq_2(nums, k):
    bucks = [[] for _ in range(len(nums))]
    counter = Counter(nums)
    for num, count in counter.items():
        bucks[count].append(num)
    i, res = len(nums) - 1, []
    while k > 0:
        if len(bucks[i]) > 0:
            res.append(*bucks[i])
            k -= len(bucks[i])
        i -= 1
    return res


if __name__ == '__main__':
    print('leetcode 332')
    print(reconstruct_itinerary([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]))
    print(reconstruct_itinerary([['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]))
    print(depth_sum([[1, 1], 2, [1, 1]]))
    print(depth_sum([1, [4, [6]]]))
    print(depth_sum_2([[1, 1], 2, [1, 1]]))
    print(depth_sum_2([1, [4, [6]]]))
    it = nested_iterator([[1, 1], 2, [1, 1]])
    for value in it:
        print(value)
    print(reverse_vowels('hello'))
    print(reverse_vowels('leetcode'))
    print(top_k_freq([1, 1, 1, 2, 2, 3], 2))
    print(top_k_freq_2([1, 1, 1, 2, 2, 3], 2))


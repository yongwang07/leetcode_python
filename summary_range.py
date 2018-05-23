def summary_range(arr):
    start = 0
    res = []
    for i in range(1, len(arr) + 1):
        if (i < len(arr) and arr[i] - arr[start] != i - start) or i == len(arr):
            res.append(f'{arr[start]}->{arr[i - 1]}' if i - 1 > start else f'{arr[start]}')
            start = i
    return res


def product_except_self(arr):
    i, j = arr[0], arr[-1]
    ret = [1 for _ in range(len(arr))]
    for k in range(1, len(arr)):
        ret[k] *= i
        ret[len(arr) - 1 - k] *= j
        i *= arr[k]
        j *= arr[len(arr) - 1 - k]
    return ret


def shortest_distance(words, word1, word2):
    a, b = -1, -1
    res = len(words)
    for index, word in enumerate(words):
        if word == word1:
            a = index
        if word == word2:
            b = index
        if a != -1 and b != -1:
            res = min(res, abs(a - b))
    return res


def shortest_distance_2(words, word1, word2):
    a, b, res = -1, -1, len(words)
    for index, word in enumerate(words):
        if word == word1:
            a = index
        elif word == word2:
            b = index
        if word == word1 and word == word2:
            a, b = b, a
        if a != -1 and b != -1:
            res = min(res, abs(a - b))
    return res


if __name__ == '__main__':
    print('leetcode 243, 245')
    print(summary_range([0, 1, 2, 4, 5, 7]))
    print(summary_range([0, 5, 8, 9, 10]))
    print(product_except_self([1, 2, 3, 4]))
    print(shortest_distance(['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'coding'))
    print(shortest_distance_2(['practice', 'makes', 'perfect', 'coding', 'makes'], 'makes', 'makes'))

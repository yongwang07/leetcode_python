from collections import deque


def word_ladder(start, end, dict):
    dict = set(dict)
    q = deque([(start, 1)])
    while len(q) > 0:
        cur, level = q.popleft()
        for i in range(len(cur)):
            for j in range(ord('a'), ord('z') + 1):
                next_word = cur[0: i] + chr(j) + cur[i+1:]
                if next_word == end:
                    return level + 1
                if next_word in dict:
                    dict.remove(next_word)
                    q.append((next_word, level + 1))
    return 0


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def reverse_word(str):
    s = list(str)
    pre = -1
    for i in range(len(s)):
        if s[i] != ' ' and pre == -1:
            pre = i
        elif s[i] == ' ' and pre != -1 and s[i - 1] != ' ':
            reverse(s, pre, i)
            pre = -1
    if pre != -1 and s[-1] != ' ':
        reverse(s, pre, len(s) - 1)
    reverse(s, 0, len(s) - 1)
    return ''.join(s)


if __name__ == '__main__':
    print('leetcode 127, 151')
    print(word_ladder('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log']))
    print("'", reverse_word('  the   sky is    blue    '), "'")

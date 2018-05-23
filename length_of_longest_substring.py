def length_of_longest_substring(s):
    m = {}
    left = 0
    max_len = 0
    start = left
    for i, c in enumerate(s):
        pre = m.get(c, None)
        if pre is None or pre < left:
            if i - left + 1 > max_len:
                max_len = i - left + 1
                start = left
        else:
            left = pre
        m[c] = i + 1
    return s[start:start + max_len]


if __name__ == '__main__':
    print('leetcode 3')
    print(length_of_longest_substring('abcabcbb'))
    print(length_of_longest_substring('pwwkew'))
    print(length_of_longest_substring('bbbbb'))

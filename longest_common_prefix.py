def longest_common_prefix(strs):
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i > len(strs[j]) or strs[j][i] != strs[0][i]:
                return strs[0][0:i]
    return strs[0]


if __name__ == '__main__':
    print('leetcode 14')
    print(longest_common_prefix(['flower', 'flow', 'flight']))
    print(longest_common_prefix(['dog', 'racecar', 'car']))
    print(longest_common_prefix(['ab', 'abcd', 'abcfg']))

def longest_palindrome(s):
    dp = [[0 for _ in range(len(s))] for _ in range(len(s))]
    left = 0
    max_len = 0
    for i in range(len(s)):
        dp[i][i] = 1
        for j in range(i):
            dp[i][j] = (s[i] == s[j] and (i - j < 2 or dp[j + 1][i - 1]))
            if dp[i][j] and max_len < i - j + 1:
                max_len = i - j + 1
                left = j
    return s[left:left + max_len]


if __name__ == '__main__':
    print('leetcode 5')
    print(longest_palindrome('babad'))

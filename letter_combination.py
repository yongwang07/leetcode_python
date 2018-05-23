def letter_combination(digits):
    maps = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    ret = []
    tmp = []

    def helper(i):
        if i == len(digits):
            ret.append(''.join(tmp))
            return
        for n in maps[int(digits[i]) - 2]:
            tmp.append(n)
            helper(i + 1)
            tmp.pop()

    helper(0)
    return ret


if __name__ == '__main__':
    print('leetcode 17')
    print(letter_combination('23'))


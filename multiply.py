def multiply(num1, num2):
    ret = [0] * (len(num1) + len(num2))
    for i in range(len(num2) - 1, -1, -1):
        cur = 0
        for j in range(len(num1) - 1, -1, -1):
            cur, ret[i + j + 1] = divmod(cur + int(num2[i]) * int(num1[j]) + ret[i + j + 1], 10)
        if cur > 0:
            ret[i] = cur
    return ''.join(map(str, ret)) if ret[0] != 0 else ''.join(map(str, ret[1:]))


if __name__ == '__main__':
    print('leetcode 43')
    print(multiply('1', '2'))
    print(multiply('45', '123'))
    print(multiply('99', '99'))
    print(multiply('9989', '9999'))
    print(multiply('3883', '988842990'))

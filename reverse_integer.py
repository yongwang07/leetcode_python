def reverse(x):
    ret = 0
    is_minus = x < 0
    x = abs(x)
    while x != 0:
        ret = 10 * ret + x % 10
        x //= 10
    return -ret if is_minus else ret


if __name__ == '__main__':
    print('leetcode 7')
    print(reverse(-123))
    print(reverse(-123456789))

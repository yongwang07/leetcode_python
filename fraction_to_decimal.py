def fraction_to_decimal(numerator, denominator):
    num, remain = divmod(numerator, denominator)
    if remain == 0:
        return str(num)
    d = dict()
    other = []
    while remain != 0:
        if remain in d:
            other[d[remain]] = '(' + other[d[remain]]
            other[-1] = other[-1] + ')'
            return str(num) + '.' + ''.join(other)
        else:
            r, a = divmod(10 * remain, denominator)
            other.append(str(r))
            d[remain] = len(other) - 1
            remain = a
    return str(num) + '.' + ''.join(other)


def excel_col(n):
    res = []
    while n > 26:
        a, n = divmod(n, 26)
        res.append(chr(ord('A') + a - 1))
    if n > 0:
        res.append(chr(ord('A') + n - 1))
    return ''.join(res)


def excel_sheet(s):
    ret = 0
    for c in s:
        ret = 26 * ret + ord(c) - ord('A') + 1
    return ret


if __name__ == '__main__':
    print('leetcode 166, 168, 171')
    print(fraction_to_decimal(2, 1))
    print(fraction_to_decimal(1, 8))
    print(fraction_to_decimal(46031, 124875))
    print(excel_col(1))
    print(excel_col(26))
    print(excel_col(28))
    print(excel_col(701))
    print('*' * 20)
    print(excel_sheet('A'))
    print(excel_sheet('AB'))
    print(excel_sheet('ZY'))

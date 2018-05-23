import itertools


def convert(s, rows):
    ret = ['' for _ in range(rows)]
    pos = itertools.cycle([x for x in range(rows)] + [x for x in range(rows - 2, 0, -1)])
    for c in s:
        ret[next(pos)] += c
    return ''.join(ret)


if __name__ == '__main__':
    print('leetcode 6')
    print(convert('PAYPALISHIRING', 3))
    print(convert('0123456789ABCDEF', 4))


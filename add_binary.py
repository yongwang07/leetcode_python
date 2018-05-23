def add_binary(a, b):
    ret = ''
    i = len(a) - 1
    j = len(b) - 1
    cur = 0
    while i >= 0 or j >= 0:
        r1 = int(a[i]) if i >= 0 else 0
        r2 = int(b[j]) if j >= 0 else 0
        cur, div = divmod(cur + r1 + r2, 2)
        ret = str(div) + ret
        i -= 1
        j -= 1
    return str(cur) + ret if cur > 0 else ret


if __name__ == '__main__':
    print('leetcode 67')
    print(add_binary('11', '1'))

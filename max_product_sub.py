def max_product_sub(arr):
    m, n, res = arr[0], arr[0], arr[0]
    for i in range(1, len(arr)):
        m = max(arr[i], n * arr[i], m * arr[i])
        n = min(arr[i], n * arr[i], m * arr[i])
        res = max(m, n, res)
    return res


def min_rotate(arr):
    left, right = 0, len(arr) - 1
    while left != right - 1:
        mid = left + (right - left) // 2
        if arr[left] < arr[mid]:
            left = mid
        else:
            right = mid
    return min(arr[left], arr[right])


def read(n):
    def read4(buff, k):
        buff[k: k + 4] = 'aaaa'
        return 4
    buffer, size = [], 0
    while n > 0:
        res = read4(buffer[size:-1], min(4, n))
        if res == 0:
            break
        size += res


def one_edit(s, t):
    if abs(len(s) - len(t)) > 1:
        return False
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            if len(s) == len(t):
                return s[i:] == t[i:]
            elif len(s) < len(t):
                return s[i:] == t[i + 1:]
            else:
                return s[i + 1:] == t[i:]
    return True


def missing_range(arr, lower, upper):
    i, j = 0, lower
    res = []
    while i < len(arr):
        if arr[i] == j:
            i += 1
            j += 1
        else:
            res.append(str(j) if arr[i] - j == 1 else f'{j}->{arr[i] - 1}')
            j = arr[i]
    if arr[-1] < upper:
        res.append(str(arr[-1] + 1) if arr[-1] - upper == 1 else f'{arr[-1] + 1}->{upper}')
    return res


def compare_version(v1, v2):
    def compare(s1, s2):
        for j in range(min(len(s1), len(s2))):
            if s1[j] != s2[j]:
                return ord(s1[j]) - ord(s2[j])
        return len(s1) - len(s2)

    s, t = v1.split('.'), v2.split('.')
    for i in range(min(len(s), len(t))):
        r = compare(s[i], t[i])
        if r != 0:
            return r
    return len(s) - len(t)


if __name__ == '__main__':
    print('leetcode 152, 153, 163, 165')
    print(max_product_sub([2, 3, -2, 4]))
    print(min_rotate([4, 5, 6, 7, 0, 1, 2]))
    print(one_edit('abc', 'abcd'))
    print(missing_range([0, 1, 3, 50, 75], 0, 99))
    print(compare_version('1.1.1.2', '1.1.1'))

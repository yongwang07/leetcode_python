def ugly_number(n):
    while n >= 2:
        if n % 2 == 0:
            n //= 2
        elif n % 3 == 0:
            n //= 3
        elif n % 5 == 0:
            n //= 5
        else:
            return False
    return n == 1


def nth_ugly_number(n):
    res = [1]
    i2, i3, i5 = 0, 0, 0
    while len(res) < n:
        m2 = res[i2] * 2
        m3 = res[i3] * 3
        m5 = res[i5] * 5
        m = min(m2, m3, m5)
        if m == m2:
            i2 += 1
        if m == m3:
            i3 += 1
        if m == m5:
            i5 += 1
        res.append(m)
    return res[-1]


def super_ugly_number(n, primes):
    res, index = [1], [0 for _ in range(len(primes))]
    while len(res) < n:
        mi, m = [0], res[index[0]] * primes[0]
        for i in range(1, len(primes)):
            if res[index[i]] * primes[i] < m:
                mi = [i]
                m = res[index[i]] * primes[i]
            elif res[index[i]] * primes[i] == m:
                mi.append(i)
        res.append(m)
        for i in mi:
            index[i] += 1
    return res[-1]


if __name__ == '__main__':
    print('leetcode 263, 264')
    print(ugly_number(11))
    print(ugly_number(12))
    print(nth_ugly_number(16))
    print(super_ugly_number(12, [2, 7, 13, 19]))

def permutation_seq(n, k):
    factor = [1 for _ in range(n)]
    for i in range(1, n):
        factor[i] = factor[i - 1] * i
    k -= 1
    res = []
    num = [i + 1 for i in range(n)]
    for i in range(n, 0, -1):
        j, k = divmod(k, factor[i - 1])
        res.append(num[j])
        num.remove(num[j])
    return res


def plus_one(digits):
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        else:
            digits[i] = 0
    return [1] + digits


def my_sqrt(x):
    left, right = 0, x
    while left < right:
        mid = left + (right - left) // 2
        if x >= mid * mid:
            left = mid + 1
        else:
            right = mid
    return right - 1


if __name__ == '__main__':
    print('leetcode 60, 66, 69')
    print(permutation_seq(4, 17))
    print(plus_one([1, 2, 3]))
    print(plus_one([1, 9]))
    import math
    print(my_sqrt(16), math.sqrt(16))
    print(my_sqrt(8), math.sqrt(8))


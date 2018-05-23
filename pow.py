def my_pow(x, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / pow(x, -n)
    else:
        half = my_pow(x, n // 2)
        return half * half if n % 2 == 0 else x * half * half


def max_sub_array(nums):
    ret = float('-inf')
    cur = 0
    for num in nums:
        cur = max(cur + num, num)
        ret = max(cur, ret)
    return ret


if __name__ == '__main__':
    print('leetcode 50, 53')
    print(my_pow(2, -3), pow(2, -3))
    print(my_pow(5, 6), pow(5, 6))
    print(my_pow(5, 7), pow(5, 7))
    print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))

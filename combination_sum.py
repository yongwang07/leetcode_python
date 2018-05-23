from copy import copy


def helper(nums, index, target, tmp, res):
    if target < 0:
        return
    if target == 0:
        res.append(copy(tmp))
        return
    for i in range(index, len(nums)):
        tmp.append(nums[i])
        helper(nums, i, target - nums[i], tmp, res)
        tmp.pop()


def combination_sum(nums, target):
    tmp = []
    res = []
    nums.sort()
    helper(nums, 0, target, tmp, res)
    return res


def helper2(nums, index, target, tmp, res):
    if target < 0:
        return
    if target == 0:
        res.append(copy(tmp))
        return
    for i in range(index, len(nums)):
        if i > index and nums[i] == nums[i - 1]:
            continue
        tmp.append(nums[i])
        helper2(nums, i + 1, target - nums[i], tmp, res)
        tmp.pop()


def combination_sum2(nums, target):
    tmp = []
    res = []
    nums.sort()
    helper2(nums, 0, target, tmp, res)
    return res


def helper3(k, n, index, tmp, res):
    if n < 0:
        return
    if n == 0 and len(tmp) == k:
        res.append(copy(tmp))
        return
    for i in range(index, n + 1):
        tmp.append(i)
        helper3(k, n - i, i + 1, tmp, res)
        tmp.pop()


def combination_sum3(k, n):
    tmp = []
    res = []
    helper3(k, n, 1, tmp, res)
    return res


def combination_sum4(nums, target):
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    for i in range(1, target + 1):
        for n in nums:
            if i >= n:
                dp[i] += dp[i - n]
    return dp[target]


if __name__ == '__main__':
    print('leetcode 39, 40, 216, 377')
    print(combination_sum([2, 3, 6, 7], 7))
    print(combination_sum2([10, 1, 2, 7, 6, 1, 5], 8))
    print(combination_sum3(3, 7))
    print(combination_sum3(3, 9))
    print(combination_sum4([1, 2, 3], 4))
from copy import copy
from collections import deque


def helper(nums, start, tmp, res):
    if start >= len(nums):
        res.append(copy(tmp))
        return
    tmp.append(nums[start])
    helper(nums, start + 1, tmp, res)
    tmp.pop()
    while start + 1 < len(nums) and nums[start + 1] == nums[start]:
        start += 1
    helper(nums, start + 1, tmp, res)


def subset(nums):
    tmp, res = [], []
    helper(nums, 0, tmp, res)
    return res


def subset_2(nums):
    q, res = deque(), []
    q.append([])
    while len(q) > 0:
        cur = q.popleft()
        res.append(list(map(lambda index: nums[index], cur)))
        start = cur[-1] + 1 if len(cur) > 0 else 0
        for i in range(start, len(nums)):
            if i == start or nums[i] != nums[i - 1]:
                q.append(cur + [i])
    return res


def decode_way(s):
    if len(s) == 0:
        return 0
    a = 0 if s[0] == '0' else 1
    for i in range(1, len(s)):
        b = a
        if s[i - 1] > '0' and int(s[i - 1: i + 1]) <= 26:
            b += 1
        a = b
    return a


if __name__ == '__main__':
    print('leetcode 78, 90, 91')
    print(subset([1, 2, 3]))
    print(subset_2([1, 2, 3]))
    print(subset([1, 2, 2]))
    print(subset_2([1, 2, 2]))
    print(decode_way('12'))
    print(decode_way('226'))

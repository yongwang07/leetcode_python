from copy import copy


def helper(nums, start, res):
    if start == len(nums):
        res.append(copy(nums))
        return
    for i in range(start, len(nums)):
        nums[start], nums[i] = nums[i], nums[start]
        helper(nums, start + 1, res)
        nums[start], nums[i] = nums[i], nums[start]


def permute(nums):
    res = []
    helper(nums, 0, res)
    return res


if __name__ == '__main__':
    print('leetcode 46')
    print(permute([1, 2, 3]))

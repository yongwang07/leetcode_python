def four_sum(nums, target):
    ret = []
    nums.sort()
    for i in range(len(nums) - 3):
        for j in range(i + 1, len(nums) - 2):
            left = j + 1
            right = len(nums) - 1
            while left < right:
                s = nums[i] + nums[j] + nums[left] + nums[right]
                if s == target:
                    ret.append((nums[i], nums[j], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif s < target:
                    left += 1
                else:
                    right -= 1
    return ret


if __name__ == '__main__':
    print('leetcode 18')
    print(four_sum([1, 0, -1, 0, -2, 2], 0))

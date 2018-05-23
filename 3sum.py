def three_sum(nums):
    nums.sort()
    ret = set()
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] + nums[i] == 0:
                ret.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif nums[left] + nums[right] > -nums[i]:
                right -= 1
            else:
                left += 1
    return ret


def three_sum_closest(nums, k):
    nums.sort()
    diff = abs(nums[0] + nums[1] + nums[2] - k)
    closest = nums[0] + nums[1] + nums[2]
    for i in range(len(nums) - 2):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[left] + nums[right] + nums[i]
            if diff > abs(sum - k):
                diff = abs(sum - k)
                closest = sum
            if sum < k:
                left += 1
            else:
                right -= 1
    return closest

if __name__ == '__main__':
    print('leetcode 15, 16')
    print(three_sum([-1, 0, 1, 2, -1, -4]))
    print(three_sum([-5, 1, 2, 3, 4]))
    print(three_sum_closest([-1, 2, 1, -4], 1))

def search_in_rotate(nums, target):
    i, j = 0, len(nums) - 1
    while i < j:
        mid = i + (j - i) // 2
        if nums[mid] == target:
            return True
        elif nums[i] == nums[mid]:
            i += 1
        elif nums[i] < nums[mid]:
            if nums[i] <= target < nums[mid]:
                j = mid - 1
            else:
                i = mid + 1
        else:
            if nums[mid] < target <= nums[j]:
                i = mid + 1
            else:
                j = mid - 1
    return False


if __name__ == '__main__':
    print('leetcode 81')
    print(search_in_rotate([2, 5, 6, 0, 0, 1, 2], 0))
    print(search_in_rotate([2, 5, 6, 0, 0, 1, 2], 3))

def binary_search(nums, target, find_left):
    left = 0
    right = len(nums) - 1
    candidate = -1
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            candidate = mid
            if find_left:
                right = mid - 1
            else:
                left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return candidate


def search(nums, target):
    left = binary_search(nums, target, True)
    if left == -1:
        return [-1, -1]
    right = binary_search(nums, target, False)
    return [left, right]


def search_insert(nums, target):
    if nums[len(nums) - 1] < target:
        return len(nums)
    left = 0
    right = len(nums) - 1
    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return right


if __name__ == '__main__':
    print('leetcode 34, 35')
    print(search([5, 7, 7, 8, 8, 10], 8))
    print(search([8, 8, 8, 8, 8, 8], 8))
    print(search([1, 2, 4, 6, 7, 9], 5))
    print(search_insert([1, 3, 5, 6], 5))
    print(search_insert([1, 3, 5, 6], 2))
    print(search_insert([1, 3, 5, 6], 7))
    print(search_insert([1, 3, 5, 6], 0))





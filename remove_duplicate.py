def remove_duplicate(nums):
    last = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[last]:
            last += 1
            nums[last] = nums[i]
    return nums[0:last + 1]


def remove_element(nums, val):
    last = -1
    for n in nums:
        if n != val:
            last += 1
            nums[last] = n
    return nums[0: last + 1]


def str_str(haystack, needle):
    if len(haystack) < len(needle):
        return -1
    for i in range(len(haystack)):
        for j in range(len(needle)):
            if needle[j] != haystack[i + j]:
                break
        if j == len(needle) - 1:
            return i
    return -1


def next_permutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = nums[len(nums) - 1: i: -1]
    return nums


def remove_duplicates(A, n):
    pre, counter, last = A[0], 1, 1
    for i in range(1, len(A)):
        if A[i] == pre and counter >= n:
            continue
        A[last] = A[i]
        last += 1
        counter += 1
        if A[i] != pre:
            counter = 1
            pre = A[i]
    return A[0:last]


if __name__ == '__main__':
    print('leetcode 26, 27, 28, 80')
    print(remove_duplicate([1, 1, 2]))
    print(remove_duplicate([1, 1, 1, 2, 2, 3, 3, 4]))
    print(remove_element([1, 3, 3, 3, 5], 3))
    print(str_str('hello', 'll'))
    print(str_str('aaaaa', 'bba'))
    print(next_permutation([1, 2, 7, 4, 3, 1]))
    print(remove_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3], 2))

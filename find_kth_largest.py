import random


def partition(list, left, right):
    init_left = left
    pivot = list[init_left]
    left += 1
    while left <= right:
        if list[left] < pivot and list[right] > pivot:
            list[left], list[right] = list[right], list[left]
            left += 1
            right -= 1
        if list[left] >= pivot:
            left += 1
        if list[right] <= pivot:
            right -= 1
    list[init_left], list[right] = list[right], list[init_left]
    return right


def find_kth_largest(seed, k):
    left = 0
    right = len(seed) - 1
    while True:
        pos = partition(seed, left, right)
        if pos == k - 1:
            return seed[pos]
        elif pos > k - 1:
            right = pos - 1
        else:
            left = pos + 1


if __name__ == '__main__':
    print('leetcode 215')
    seed = [random.randrange(1, 100) for _ in range(10)]
    r = find_kth_largest(seed, 4)
    print(seed, '4th', '=', r)
    r = find_kth_largest([3, 2, 1, 5, 6, 4], 2)
    print([3, 2, 1, 5, 6, 4], r)

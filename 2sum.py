from collections import defaultdict
from operator import itemgetter

# leetcode code 1 and 167 and 170 and 653


def two_sum(nums, target):
    m = defaultdict(list)
    ret = []
    for i, num in enumerate(nums):
        if len(m[target - num]) > 0:
            another = m[target - num].pop()
            ret.append([i, another])
        else:
            m[num].append(i)
    return ret


def two_sum_2(nums, target):
    ret = []
    num_with_index = [(i, num) for i, num in enumerate(nums)]
    num_with_index.sort(key=itemgetter(1))
    i, j = 0, len(num_with_index) - 1
    while i < j:
        if num_with_index[i][1] + num_with_index[j][1] == target:
            ret.append([num_with_index[i][0], num_with_index[j][0]])
            i += 1
            j -= 1
        elif num_with_index[i][1] + num_with_index[j][1] < target:
            i += 1
        else:
            j -= 1
    return ret


class TwoSum:
    def __init__(self):
        self.nums = defaultdict(int)

    def add(self, num):
        self.nums[num] += 1

    def find(self, target):
        for key in list(self.nums.keys()):
            if target - key == key and self.nums[key] >= 2:
                return True
            if target - key != key and self.nums[target - key] > 0:
                return True
        return False


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def two_sum_3(r, target):
    ret = []
    s = defaultdict(int)

    def helper(node):
        if node is None:
            return
        helper(node.left)
        if s[target - node.value] > 0:
            ret.append((target - node.value, node.value))
            s[target - node.value] -= 1
        else:
            s[node.value] += 1
        helper(node.right)

    helper(r)
    return ret


def pre_order(node):
    if node is None:
        return
    pre_order(node.left)
    print(node.value)
    pre_order(node.right)


if __name__ == '__main__':
    print('leetcode 2 sum')
    print(two_sum([2, 7, 11, 6, 15, 3], 9))
    print(two_sum_2([2, 7, 11, 6, 15, 3], 9))
    two_sum = TwoSum()
    two_sum.add(5)
    print(two_sum.find(10))
    two_sum.add(5)
    two_sum.add(10)
    two_sum.add(10)
    print(two_sum.find(10))
    root = Node(5)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.right = Node(4)
    root.right = Node(6)
    root.right.right = Node(7)
    print(two_sum_3(root, 9))

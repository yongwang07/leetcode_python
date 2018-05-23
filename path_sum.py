from binary_tree import Node


def helper(node, value):
    if node is None:
        return 0
    r = 0
    if node.value == value:
        r = 1
    return r + helper(node.left, value - node.value) + helper(node.right, value - node.value)


def path_sum(root, sum):
    if root is None:
        return 0
    return helper(root.left, sum - root.value) + helper(root.right, sum - root.value) + helper(root.left, sum) \
        + helper(root.right, sum)


def parse_ternary(express):
    st, n, num = [], len(express), ''
    for i in range(n):
        c = express[n - i - 1]
        if c == ':':
            if len(num):
                st.append(num)
                num = ''
        elif c == '?':
            if len(num):
                st.append(num)
                num = ''
            st.append(c)
        elif (c == 'T' or c == 'F') and st[-1] == '?':
            st.pop()
            t = st.pop()
            f = st.pop()
            st.append(t if c == 'T' else f)
        else:
            num = c + num
    return st.pop()


def find_disappear_number(nums):
    i = 0
    while i < len(nums):
        if nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        else:
            i += 1
    return [i for i, v in enumerate(nums) if i != v - 1]


if __name__ == '__main__':
    print('leetcode 437')
    root = Node(10)
    root.left = Node(5)
    root.left.left = Node(3)
    root.left.right = Node(2)
    root.left.left.left = Node(3)
    root.left.left.right = Node(-2)
    root.left.right = Node(2)
    root.left.right.right = Node(1)
    root.right = Node(-3)
    root.right.right = Node(11)
    print(path_sum(root, 8))
    print(parse_ternary('T?2:3'))
    print(parse_ternary('F?1:T?4:5'))
    print(parse_ternary('T?T?F:5:3'))
    print(find_disappear_number([4, 3, 2, 7, 8, 2, 3, 1]))
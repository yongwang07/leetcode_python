from binary_tree import Node, in_order


def long_consecutive_seq(root):
    max_len_path = 0

    def dfs(node, pre_node, level):
        if node is None:
            return
        if pre_node is not None and node.value == pre_node.value + 1:
            cur_level = level + 1
        else:
            cur_level = 1
        nonlocal max_len_path
        max_len_path = max(max_len_path, cur_level)
        dfs(node.left, node, cur_level)
        dfs(node.right, node, cur_level)

    dfs(root, None, 0)
    return max_len_path


def long_increase_sub(arr):
    dp = [1 for _ in range(len(arr))]
    max_len = 0
    for i in range(1, len(arr)):
        m = 1
        for j in range(i):
            if arr[i] > arr[j]:
                m = max(m, dp[j] + 1)
        dp[i] = max(m, dp[i])
        max_len = max(max_len, m)
    return max_len


def helper(s, first, second):
    if len(s) == 0:
        return True
    if first is None or second is None:
        for i in range(len(s)):
            if s[0:i+1][0] == '0':
                continue
            if first is None:
                first = int(s[0:i + 1])
            else:
                second = int(s[0:i + 1])
            if helper(s[i + 1:], first, second):
                return True
        return False
    else:
        ss = str(first + second)
        if s.startswith(ss):
            return helper(s[len(ss) - 1:], second, first + second)
        else:
            return False


def is_additive_number(str):
    return helper(str, None, None)


if __name__ == '__main__':
    print('leetcode 298, 300, 306')
    root = Node(1)
    root.right = Node(3)
    root.right.left = Node(2)
    root.right.right = Node(4)
    root.right.right.right = Node(5)
    print(long_consecutive_seq(root))
    root = Node(2)
    root.right = Node(3)
    root.right.left = Node(2)
    root.right.left.left = Node(1)
    print(long_consecutive_seq(root))
    print(long_increase_sub([10, 9, 2, 5, 3, 7, 101, 18]))
    print(is_additive_number('112358'))
    print(is_additive_number('199100199'))


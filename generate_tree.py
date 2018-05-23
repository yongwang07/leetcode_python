from binary_tree import Node, in_order


def helper(start, end):
    if start >= end:
        return [None] if start > end else [Node(start)]
    res = []
    for i in range(start, end):
        left = helper(start, i)
        right = helper(i + 1, end)
        for j in left:
            for k in right:
                node = Node(i)
                node.left = j
                node.right = k
                res.append(node)
    return res


def generate_tree(n):
    return helper(1, n + 1)


if __name__ == '__main__':
    print('leetcode 95')
    for r in generate_tree(3):
        print(in_order(r))


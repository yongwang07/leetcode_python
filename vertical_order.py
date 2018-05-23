from collections import defaultdict, Counter
from binary_tree import Node
from operator import itemgetter


def vertical_order(root):
    m = defaultdict(list)

    def helper(node, level):
        if node is None:
            return
        m[level].append(node.value)
        helper(node.left, level - 1)
        helper(node.right, level + 1)
    helper(root, 0)
    return list(map(itemgetter(1), sorted(m.items(), key=itemgetter(0))))


def remove_duplicate(s):
    visited, count, st = set(), Counter(s), []
    for c in s:
        if c in visited:
            continue
        while len(st) > 0 and ord(c) < ord(st[-1]) and count[st[-1]] > 0:
            visited.remove(st.pop())
        count[c] -= 1
        visited.add(c)
        st.append(c)
    return ''.join(st)


def generate_abbre(word):
    tmp, res = [], []

    def helper(start):
        if start == len(word):
            res.append(''.join(tmp))
            return
        tmp.append(word[start])
        helper(start + 1)
        tmp.pop()
        merge = False
        if len(tmp) > 0 and tmp[-1].isdigit():
            tmp[-1] = str(int(tmp[-1]) + 1)
            merge = True
        else:
            tmp.append(str(1))
        helper(start + 1)
        if merge:
            tmp[-1] = str(int(tmp[-1]) - 1)
        else:
            tmp.pop()
    helper(0)
    return res


if __name__ == '__main__':
    print('leetcode 313, 320')
    root = Node(3)
    root.left = Node(9)
    root.right = Node(20)
    root.right.left = Node(15)
    root.right.right = Node(7)
    print(vertical_order(root))
    root = Node(3)
    root.left = Node(9)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(20)
    root.right.left = Node(2)
    root.right.right = Node(7)
    print(vertical_order(root))
    print(remove_duplicate('bcabc'))
    print(remove_duplicate('cbacdcbc'))
    print(generate_abbre('word'))

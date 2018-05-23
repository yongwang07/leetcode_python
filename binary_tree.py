class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None


def in_order(node):
    res = []
    if node is None:
        return

    def order(node):
        if node is None:
            return
        order(node.left)
        res.append(node.value)
        order(node.right)

    order(node)
    return res


def in_order_iter(head):
    res, st = [], []
    while head is not None or len(st) > 0:
        while head is not None:
            st.append(head)
            head = head.left
        top = st.pop()
        res.append(top.value)
        head = top.right
    return res


class BSTIterator:
    def __init__(self, root):
        self.st = []
        while root is not None:
            self.st.append(root)
            root = root.left

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.st) == 0:
            raise StopIteration
        ret = self.st.pop()
        r = ret.right
        while r is not None:
            self.st.append(r)
            r = r.left
        return ret


if __name__ == '__main__':
    print('leetcode 94, 173')
    h = Node(1)
    h.right = Node(2)
    h.right.left = Node(3)
    print(in_order(h))
    print(in_order_iter(h))
    root = Node(6)
    root.left = Node(4)
    root.left.left = Node(2)
    root.left.right = Node(5)
    root.right = Node(11)
    root.right.left = Node(7)
    root.right.left.right = Node(9)
    it = BSTIterator(root)
    for node in it:
        print(node.value, end=',')

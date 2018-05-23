class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def visit(node):
    ret = []
    while node is not None:
        ret.append(node.value)
        node = node.next
    return '=>'.join(map(str, ret))


def remove_nth_node_from_end(node, k):
    end = node
    i = 0
    while end is not None and i < k:
        end = end.next
        i += 1
    if i < k:
        return node
    first = node
    while end.next is not None:
        end = end.next
        first = first.next
    first.next = first.next.next
    return node


if __name__ == '__main__':
    print('leetcode 19')
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print(visit(head))
    print(visit(remove_nth_node_from_end(head, 2)))

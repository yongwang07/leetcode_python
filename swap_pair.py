from remove_nth_node_from_end import Node, visit


def swap_pair(head):
    print(head)
    h = Node(0)
    last = h
    one = head
    while one is not None:
        second = one.next
        if second is None:
            last.next = one
            break
        temp = second.next
        last.next = second
        second.next = one
        one.next = None
        last = one
        one = temp
    return h.next


if __name__ == '__main__':
    print('leetcode 24')
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print(visit(swap_pair(head)))

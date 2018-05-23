from remove_nth_node_from_end import visit, Node


def reverse_link(head, m, n):
    dummy = Node(0)
    dummy.next = head
    count, first, last = 0, dummy, dummy
    while count < m:
        first = last
        last = last.next
        count += 1
    forward = last.next
    count += 1
    while count <= n:
        last.next = forward.next
        forward.next = first.next
        first.next = forward
        forward = last.next
        count += 1
    return dummy.next


if __name__ == '__main__':
    print('leetcode 92')
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print(visit(reverse_link(head, 2, 5)))

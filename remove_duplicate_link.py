from remove_nth_node_from_end import visit, Node


def remove_duplicate_link(head):
    first = head
    count = 1
    h = Node(0)
    last = h
    while first is not None:
        second = first.next
        while second is not None and second.value == first.value:
            count += 1
            second = second.next
        if count == 1:
            last.next = first
            last = last.next
        first = second
        count = 1
    return h.next


def delete_duplicate(head):
    h, last, forward = head, head.next, head.next
    while forward is not None:
        if forward.value != last.value:
            last.next = forward
            last = last.next
        forward = forward.next
        last.next = None
    return h.next


def partition(head, k):
    heads = [Node(0) for _ in range(2)]
    lasts = [last for last in heads]
    while head is not None:
        i = 0
        if head.value < k:
            lasts[0].next = head
        else:
            lasts[1].next = head
            i = 1
        head = head.next
        lasts[i] = lasts[i].next
        lasts[i].next = None
    lasts[0].next = heads[1].next
    return heads[0].next


if __name__ == '__main__':
    print('leetcode 82, 83, 86')
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(4)
    head.next.next.next.next.next.next = Node(5)
    print(visit(head))
    print(visit(remove_duplicate_link(head)))
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(1)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(3)
    print(visit(remove_duplicate_link(head)))
    head = Node(100)
    print(visit(remove_duplicate_link(head)))
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    print(visit(delete_duplicate(head)))
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(3)
    head.next.next.next.next = Node(3)
    print(visit(delete_duplicate(head)))
    head = Node(1)
    head.next = Node(4)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(2)
    print('*' * 20)
    print(visit(partition(head, 3)))

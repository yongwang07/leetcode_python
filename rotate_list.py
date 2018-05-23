from remove_nth_node_from_end import visit, Node


def rotate_right(head, k):
    if head is None:
        return None
    cur = head
    n = 0
    while cur is not None:
        n += 1
        cur = cur.next
    k %= n
    fast = head
    slow = head
    for i in range(k):
        if fast is None:
            break
        fast = fast.next
    if fast is None:
        return head
    while fast.next is not None:
        fast = fast.next
        slow = slow.next
    fast.next = head
    fast = slow.next
    slow.next = None
    return fast


if __name__ == '__main__':
    print('leetcode 61')
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    print(visit(head))
    print(visit(rotate_right(head, 2)))

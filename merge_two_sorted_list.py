from remove_nth_node_from_end import Node as Base, visit
from queue import PriorityQueue
from functools import total_ordering


@total_ordering
class Node(Base):
    def __init__(self, value):
        super().__init__(value)

    def __le__(self, other):
        return self.value < other.value


def merge_two_sorted_list(h1, h2):
    head = Node(0)
    last = head
    while h1 is not None and h2 is not None:
        if h1.value < h2.value:
            last.next = h1
            h1 = h1.next
        else:
            last.next = h2
            h2 = h2.next
        last = last.next
    last.next = h1 if h1 is not None else h2
    return head.next


def merge_k_sorted_list(nodes):
    q = PriorityQueue()
    for node in nodes:
        q.put(node)
    head = Node(0)
    last = head
    while q.qsize() > 0:
        node = q.get()
        last.next = node
        last = last.next
        if node.next is not None:
            q.put(node.next)
    return head.next


def merge_sorted_array(A, m, B, n):
    last = m + n - 1
    m -= 1
    n -= 1
    while n >= 0 and m >= 0:
        if A[m] < B[n]:
            A[last] = B[n]
            n -= 1
        else:
            A[last] = A[m]
            m -= 1
        last -= 1
    while n >= 0:
        A[last] = B[n]
        n -= 1
        last -= 1
    return A


if __name__ == '__main__':
    print('leetcode 21, 23, 88')
    h1 = Node(1)
    h1.next = Node(2)
    h1.next.next = Node(4)
    h2 = Node(1)
    h2.next = Node(3)
    h2.next.next = Node(4)
    r = merge_two_sorted_list(h1, h2)
    print(visit(r))
    print('*' * 20)
    h3 = Node(1)
    h3.next = Node(4)
    h3.next.next = Node(5)
    h4 = Node(1)
    h4.next = Node(3)
    h4.next.next = Node(4)
    h5 = Node(2)
    h5.next = Node(6)
    r = merge_k_sorted_list([h3, h4, h5])
    print(visit(r))
    print(merge_sorted_array([1, 2, 3, 0, 0, 0], 3, [12, 15, 16], 3))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


def print_list(list):
    while list is not None:
        print(list.value, end=',')
        list = list.next
    print()


def add_two_number(list1, list2):
    cur = 0
    first = Node(0)
    last = first
    while list1 is not None or list2 is not None:
        r1 = list1.value if list1 is not None else 0
        r2 = list2.value if list2 is not None else 0
        value = cur + r1 + r2
        last.next = Node(value % 10)
        cur = value // 10
        list1 = list1.next
        list2 = list2.next
        last = last.next
    return first.next


if __name__ == '__main__':
    print('leetcode 2')
    list1 = Node(2)
    list1.next = Node(4)
    list1.next.next = Node(3)
    list2 = Node(5)
    list2.next = Node(6)
    list2.next.next = Node(4)
    r = add_two_number(list1, list2)
    print_list(r)

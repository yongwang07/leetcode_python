from binary_tree import Node
from reverse_link import Node as LinkNode, visit
import heapq

def remove(pre, node, res):
    if node.left is None and node.right is None:
        if pre.left == node:
            pre.left = None
        else:
            pre.right = None
        res.append(node.value)
        return
    if node.left is not None:
        remove(node, node.left, res)
    if node.right is not None:
        remove(node, node.right, res)


def find_binary_leaf(root):
    res = []
    while root.left is not None or root.right is not None:
        tmp = []
        if root.left is not None:
            remove(root, root.left, tmp)
        if root.right is not None:
            remove(root, root.right, tmp)
        res.append([*tmp])
    res.append([root.value])
    return res


def plus_one(head):
    h = Node(0)
    h.next = head
    cur = h
    while cur.next is not None and cur.next.value != 9:
        cur = cur.next
    cur.value += 1
    cur = cur.next
    while cur is not None:
        cur.value = 0
        cur = cur.next
    return h.next if h.value == 0 else h


def k_smallest_pair(nums1, nums2, k):
    q, res = [(nums1[0] + nums2[0], 0, 0)], []
    while k > 0:
        a, b = heapq.heappop(q)[1:]
        res.append((nums1[a], nums2[b]))
        k -= 1
        if a + 1 < len(nums1):
            heapq.heappush(q, (nums1[a + 1] + nums2[b], a + 1, b))
        if b + 1 < len(nums2):
            heapq.heappush(q, (nums1[a] + nums2[b + 1], a, b + 1))
    return res


if __name__ == '__main__':
    print('leetcode 366')
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right = Node(3)
    print(find_binary_leaf(root))
    head = LinkNode(1)
    head.next = LinkNode(2)
    head.next.next = LinkNode(3)
    print(visit(plus_one(head)))
    head = LinkNode(1)
    head.next = LinkNode(9)
    print(visit(plus_one(head)))
    print(k_smallest_pair([1, 7, 11], [2, 4, 6], 3))
    print(k_smallest_pair([1, 1, 2], [1, 2, 3], 2))



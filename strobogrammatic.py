from collections import defaultdict

def strobogrammatic(num):
    s = {'0', '1', '8', '6', '9'}
    i, j = 0, len(num) - 1
    while i <= j:
        if (num[i] == num[j] and num[i] not in s) or (num[i] != num[j] and {num[i], num[j]} != {'6', '9'}):
            return False
        i += 1
        j -= 1
    return True


def helper(tmp, start, end, res):
    if start > end:
        res.append(''.join(tmp))
        return
    for key, value in {'0': '0', '1': '1', '8': '8', '6': '9', '9': '6'}.items():
        if start == end and key in {'6', '9'}:
            continue
        if start == 0 and key == '0':
            continue
        tmp[start] = key
        tmp[end] = value
        helper(tmp, start + 1, end - 1, res)


def gen_strobogrammatic(n):
    tmp, res = [None for _ in range(n)], []
    helper(tmp, 0, n - 1, res)
    return res


def group_shift(arr):
    d = defaultdict(list)
    for word in arr:
        key = ''.join(map(lambda x: str((ord(x) - ord(word[0]) + 26) % 26), list(word)))
        d[key].append(word)
    return list(d.values())


class Array2D:
    def __init__(self, arr):
        self.arr = arr
        self.row = self.col = 0
        self._move()

    def _move(self):
        while self.row < len(self.arr):
            if self.col >= len(self.arr[self.row]):
                self.row += 1
                self.col = 0
            else:
                break

    def __iter__(self):
        return self

    def __next__(self):
        if self.row >= len(self.arr):
            raise StopIteration
        r = self.arr[self.row][self.col]
        self.col += 1
        self._move()
        return r


if __name__ == '__main__':
    print('leetcode 246, 247, 251')
    print(strobogrammatic('99166'))
    print(gen_strobogrammatic(4))
    print(group_shift(['abc', 'bcd', 'acef', 'xyz', 'az', 'ba', 'a', 'z']))
    it = Array2D([[1, 2], [3], [4, 5, 6]])
    for value in it:
        print(value, end=',')

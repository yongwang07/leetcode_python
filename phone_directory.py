import random


class PhoneDirectory:
    def __init__(self, size):
        self.v = [i for i in range(size)]
        self.m = dict((i, i) for i in range(size))

    def get(self):
        if len(self.v) == 0:
            return -1
        index = random.randint(0, len(self.v) - 1)
        number = self.v[index]
        if index != len(self.v) - 1:
            self.m[self.v[-1]] = index
            self.v[index] = self.v[-1]
        self.m.pop(number)
        self.v.pop()
        return number

    def check(self, number):
        return number in self.m

    def release(self, number):
        if number in self.m:
            return
        self.v.append(number)
        self.m[number] = len(self.v) - 1


def deserialize(s):
    num, st = None, []
    for c in s:
        if c.isdigit():
            num = int(c) if num is None else 10 * num + int(c)
        elif c == '[':
            st.append('[')
        elif c == ',':
            st.append(num)
            num = None
        elif c == ']':
            if num is not None:
                st.append(num)
                num = None
            collect = []
            while st[-1] != '[':
                collect.insert(0, st.pop())
            st.pop()
            st.append(collect)
    if num is not None:
        st.append(num)
    return st.pop()


def length_longest_path(input):
    m, res, long_str = {0: 0}, 0, ''
    for path in input.split('\n'):
        level = path.count('\t')
        file = path[level * len('\t'):]
        if file.find('.') != -1:
            if res < len(m[level]) + len(file):
                res = len(m[level]) + len(file)
                long_str = file
                while level > 0:
                    long_str = f'{m[level]}/{long_str}'
                    level -= 1
        else:
            m[level + 1] = file
    return long_str


def valid_utf8(data):
    bits = 0
    while (data[0] << bits) & 0x80 != 0:
        bits += 1
    if bits == 0:
        return len(data) == 1
    if (data[0] << (bits + 1)) & 0x80 != 0:
        return False
    bits -= 1
    for i in range(1, len(data)):
        if bits == 0:
            return True
        if data[i] & 0xC0 == 0:
            return False
        bits -= 1
    return False


if __name__ == '__main__':
    print('leetcode 379')
    p = PhoneDirectory(10)
    number = p.get()
    print(p.check(number))
    print(deserialize('324'))
    print(deserialize('[123, [456, [789]]]'))
    print(deserialize('[123, [456, [0]]]'))
    print(length_longest_path('dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext'))
    print(length_longest_path('dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\t'
                              'subsubdir2\n\t\t\tfile2.ext'))
    print(valid_utf8([197, 130, 1]))
    print(valid_utf8([235, 140, 4]))

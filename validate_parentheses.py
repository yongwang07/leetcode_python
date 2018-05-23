def is_validate_parentheses(s):
    st = []
    pair = {'}': '{', ']': '[', ')': '('}
    for c in s:
        if c in pair.values():
            st.append(c)
        else:
            if len(st) == 0:
                return False
            if pair.get(c, None) != st.pop():
                return False
    return len(st) == 0


def generate_parentheses(n):
    ret = []

    def helper(left, right, tmp):
        if left > right:
            return
        if left == right and left == 0:
            ret.append(tmp)
        else:
            if left > 0:
                helper(left - 1, right, tmp + '(')
            if right > 0:
                helper(left, right - 1, tmp + ')')
    helper(n, n, '')
    return ret


if __name__ == '__main__':
    print('leetcode 20, 22')
    print(is_validate_parentheses('()'))
    print(is_validate_parentheses('()[]{}'))
    print(is_validate_parentheses('([)]'))
    print(is_validate_parentheses('(]'))
    print(generate_parentheses(3))


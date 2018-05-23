def calculator(s):
    res, sign, num = 0, '+', 0
    for c in s:
        if c != ' ' and c != '(' and c != ')':
            if c == '+' or c == '-':
                num = num if sign == '+' else -num
                res += num
                sign = c
                num = 0
            else:
                num = 10 * num + int(c)
    if num != 0:
        num = num if sign == '+' else -num
        res += num
    return res


def calculator_2(s):
    res, a, b, num, sign = 0, None, None, 0, None
    op = {'+': 1, '-': 1, '*': 2, '/': 2}
    fn = {'+': lambda a, b: a + b, '-': lambda a, b: a - b, '*': lambda a, b: a * b, '/': lambda a, b: a // b}
    for c in s:
        if c.isdigit():
            num = 10 * num + int(c)
        elif c in op.keys():
            if a is None:
                a = num
            elif b is None:
                b = num
            num = 0
            if a is not None and b is not None:
                if op[sign] >= op[c]:
                    a = fn[sign](a, b)
                    b = None
                elif op[sign] < op[c]:
                    res += a
                    a = -b if sign == '-' else b
                    b = None
            sign = c
    res += fn[sign](a, num)
    return res


def calculator_3(s):
    op_st, num_st = [], []
    fn = {'+': lambda x, y: x + y,
          '-': lambda x, y: x - y,
          '*': lambda x, y: x * y,
          '/': lambda x, y: x // y}
    order = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
    num = 0
    for c in s:
        if c == ' ':
            continue
        if c.isdigit():
            num = 10 * num + int(c)
        elif c == '(':
            op_st.append('(')
        else:
            if num > 0:
                num_st.append(num)
                num = 0
            if c == ')':
                while op_st[-1] != '(':
                    op = op_st.pop()
                    b = num_st.pop()
                    a = num_st.pop()
                    num_st.append(fn[op](a, b))
                op_st.pop()
            else:
                while len(op_st) > 0 and order[c] <= order[op_st[-1]]:
                    op = op_st.pop()
                    b = num_st.pop()
                    a = num_st.pop()
                    num_st.append(fn[op](a, b))
                op_st.append(c)
    if num > 0:
        num_st.append(num)
    while len(op_st) > 0:
        op = op_st.pop()
        b = num_st.pop()
        a = num_st.pop()
        num_st.append(fn[op](a, b))
    return num_st[-1]


if __name__ == '__main__':
    print('leetcode 224')
    print(calculator(' 11 + 1 '))
    print(calculator(' 12-1 -2'))
    print(calculator('(100 + (4 + 5 + 2) -3) + (6 + 8)'))
    print(calculator_2('3-2*2'))
    print(calculator_2('3/2'))
    print(calculator_2('3+5/2'))
    print('*' * 20)
    print(calculator_3('(2+6*3+5-(3*14/7+2)*5)+3'))


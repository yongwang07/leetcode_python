def validate(s):
    if len(s) > 3 or (len(s) > 1 and s[0] == '0'):
        return False
    return 0 <= int(s) <= 255


def helper(s, start, tmp, res):
    if start == len(s) and len(tmp) == 4:
        res.append('.'.join(tmp))
        return
    for i in range(start, len(s)):
        ip = s[start: i + 1]
        if validate(ip):
            tmp.append(ip)
            helper(s, i + 1, tmp, res)
            tmp.pop()


def restore_ip(s):
    tmp, res = [], []
    helper(s, 0, tmp, res)
    return res


if __name__ == '__main__':
    print('leetcode 93')
    print(restore_ip('25525511135'))

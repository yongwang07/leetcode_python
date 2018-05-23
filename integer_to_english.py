def convert_hundred(n):
    unit = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten',
            'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen',
            'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
    ret = ''
    while n > 0:
        if 0 < n <= 19:
            ret = f'{ret} {unit[n]}'
            return ret.strip()
        elif 20 <= n <= 99:
            ret = f'{ret} {unit[18 + n//10]}'
            n %= 10
        elif n >= 100:
            ret = f'{ret} {unit[n//100]} Hundred'
            n %= 100


def integer_to_english(n):
    unit = ['Billion', 'Million', 'Thousand', '']
    ret, i = '', len(unit) - 1
    while n > 0:
        n, r = divmod(n, 1000)
        if r > 0:
            ret = f'{convert_hundred(r)} {unit[i]} {ret}'
        i -= 1
    return ret.strip()


def paint_fence(n, k):
    if n == 0:
        return 0
    same, diff = 0, k
    for i in range(2, n + 1):
        t = diff
        diff = (same + diff) * (k - 1)
        same = t
    return same + diff


if __name__ == '__main__':
    print('leetcode 273, 276')
    print(integer_to_english(103))
    print(integer_to_english(12345))
    print(integer_to_english(1234567))
    print(integer_to_english(2147483647))
    print(paint_fence(2, 3))

def count_and_say(n):
    curr = '1'
    step = 1
    while step < n:
        counter = 0
        pre = curr[0]
        tmp = ''
        for c in curr:
            if counter == 0 or c == pre:
                counter += 1
            else:
                tmp += f'{counter}{pre}'
                counter = 1
                pre = c
        if counter > 0:
            tmp += f'{counter}{pre}'
        curr = tmp
        step += 1
    return curr


if __name__ == '__main__':
    print('leetcode 38')
    print(count_and_say(5))

def is_palindrome(x):
    div = 1
    while x // div > 10:
        div *= 10
    while x != 0:
        left = x // div
        right = x % 10
        if left != right:
            return False
        x = (x % div) // 10
        div = div / 100
    return True


if __name__ == '__main__':
    print('leetcode 9')
    print(is_palindrome(121))
    print(is_palindrome(5445))
    print(is_palindrome(1234564321))

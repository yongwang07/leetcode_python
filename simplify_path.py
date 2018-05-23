def simplify_path(path):
    dirs = [d for d in path.split('/') if d != '']
    st = []
    for d in dirs:
        if d == '.' or d == ' ':
            continue
        if d == '..':
            if len(st) > 0:
                st.pop()
        else:
            st.append(d)
    return '/' + '/'.join(st)


def set_zero(matrix):
    m, n = len(matrix), len(matrix[0])
    is_row_zero, is_col_zero = False, False
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                if i == 0:
                    is_row_zero = True
                if j == 0:
                    is_col_zero = True
                matrix[0][j] = 0
                matrix[i][0] = 0
    for i in range(1, n):
        if matrix[0][i] == 0:
            for row in range(1, m):
                matrix[row][i] = 0
        elif is_col_zero is True:
            matrix[0][i] = 0
    for i in range(1, m):
        if matrix[i][0] == 0:
            for col in range(1, n):
                matrix[i][col] = 0
        elif is_row_zero is True:
            matrix[i][0] = 0
    return matrix


def sort_colors(nums):
    left, right = 0, len(nums) - 1
    for i in range(len(nums)):
        if i > right:
            break
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
        elif nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
            i -= 1
    return nums


if __name__ == '__main__':
    print('leetcode 71, 73')
    print(simplify_path('/home/'))
    print(simplify_path('/a/./b/../../c/'))
    print(simplify_path('/../'))
    print(simplify_path('/home//foo'))
    print(set_zero([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
    print(set_zero([[1, 1, 2, 0], [0, 4, 5, 2], [1, 3, 1, 5]]))
    print(sort_colors([2, 0, 2, 1, 1, 0]))
    print(sort_colors([2, 0, 1]))

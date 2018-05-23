def merge(times):
    times.sort()
    ret = []
    start, end = times[0]
    for i in range(1, len(times)):
        if times[i][0] > end:
            ret.append([start, end])
            start, end = times[i][0], times[i][1]
        else:
            end = max(end, times[i][1])
    ret.append([start, end])
    return ret


def insert_merge(times, insert):
    start, end = insert
    ret = []
    for i, interval in enumerate(times):
        if interval[1] < start:
            ret.append(interval)
        elif interval[0] > end:
            ret.append([start, end])
            ret.extend(times[i:])
            return ret
        else:
            start = min(start, interval[0])
            end = max(end, interval[1])
    ret.append([start, end])
    return ret


def employee_free_time(schedules):
    intervals = sorted([interval for schedule in schedules for interval in schedule])
    start, end = intervals[0]
    ret = []
    for i in range(1, len(intervals)):
        if intervals[i][0] <= end:
            end = max(intervals[i][1], end)
        else:
            ret.append([end, intervals[i][0]])
            start, end = intervals[i]
    return ret


def length_of_last_word(s):
    end = -1
    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ' and (i + 1 == len(s) or s[i + 1] == ' '):
            end = i
        if s[i] == ' ' and i + 1 < len(s) and s[i + 1] != ' ':
            return end - i
    return end + 1 if end != -1 else 0


if __name__ == '__main__':
    print('leetcode 56, 57, 759')
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
    print(insert_merge([[1, 3], [6, 9]], [2, 5]))
    print(insert_merge([[8, 13], [16, 19]], [2, 5]))
    print('*' * 20)
    print(employee_free_time([[[1, 2], [5, 6]], [[1, 3]], [[4, 10]]]))
    print(employee_free_time([[[1, 3], [6, 7]], [[2, 4]], [[2, 5], [9, 12]]]))
    print(length_of_last_word('Hello World'))
    print(length_of_last_word(' Hello World  '))
    print(length_of_last_word('abcd '))

from collections import defaultdict


def rotate_image(image):
    n = len(image)
    origin_x, origin_y = 0, 0
    while origin_x < n and origin_y < n:
        x, y = origin_x, origin_y
        while x < n and y < n:
            image[x][origin_y], image[origin_x][y] = image[origin_x][y], image[x][origin_y]
            x += 1
            y += 1
        image[origin_x].reverse()
        origin_x += 1
        origin_y += 1
    return image


def group_anagrams(strs):
    group = defaultdict(list)
    for s in strs:
        key = ''.join(sorted(list(s)))
        group[key].append(s)
    return list(group.values())


if __name__ == '__main__':
    print('leetcode 48, 49')
    print(rotate_image([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(list('abc'))
    print(group_anagrams(['eat', 'tea', 'tan', 'ate', 'nat', 'bat']))

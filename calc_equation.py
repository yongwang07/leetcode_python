from collections import defaultdict


def dfs(s, m, visited, tmp, e):
    if s == e:
        return True
    for neighbor, value in m[s]:
        if neighbor not in visited:
            tmp[-1] *= value
            visited.add(neighbor)
            if dfs(neighbor, m, visited, tmp, e):
                return True
            tmp[-1] /= value
            visited.remove(neighbor)
    return False


def cal_equation(equations, values, querys):
    m = defaultdict(list)
    for start, end, value in zip(*equations, values):
        m[start].append((end, value))
        m[end].append((start, 1/value))
    res = [-1.0] * len(querys)
    for i, [s, e] in enumerate(querys):
        if s not in m.keys() and e not in m.keys():
            res[i] = -1.0
            continue
        visited, tmp = set(s), [1.0]
        if dfs(s, m, visited, tmp, e):
            res[i] = tmp[-1]
    return res


def reconstruct_queue(peoples):
    peoples.sort(key=lambda people: [-people[0], people[1]])
    res = []
    for people in peoples:
        res.insert(people[1], people)
    return res


def valid_word_abbreviation(word, abbr):
    i, j = 0, 0
    while i < len(word) and j < len(abbr):
        if word[i] == abbr[j]:
            i += 1
            j += 1
            continue
        if abbr[j].isdigit():
            num = 0
            while j < len(abbr) and abbr[j].isdigit():
                num = 10 * num + int(abbr[j])
                j += 1
            i += num
        else:
            return False
    return i == len(word) and j == len(abbr)


if __name__ == '__main__':
    print('leetcode 399')
    print(cal_equation([['a', 'b'], ['b', 'c']], [2.0, 3.0], [['a', 'c'], ['b', 'a'], ['a', 'e'], ['a', 'a']]))
    print(reconstruct_queue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))
    print(valid_word_abbreviation('internationalization', 'i12iz4n'))
    print(valid_word_abbreviation('apple', 'a2e'))
    print(valid_word_abbreviation('word', '4'))

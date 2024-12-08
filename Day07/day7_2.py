# Filename: day7_2.py
# Author: Maxime Zammit
# Created: 2024-12-08
# Description: Equation patcher (w. extra operator)


def compute(res, terms):
    my_map = [0, 1]
    is_first = True
    for term in terms:
        temp_map = []
        for x in my_map:
            temp_map.append(x * term)
            temp_map.append(x + term)
            if not is_first:
                temp_map.append(int(str(x)+str(term)))
        if is_first:
            temp_map.append(x)
            is_first = False
        my_map = temp_map.copy()
    return res in my_map

sum = 0

inp = open("input.txt", 'r')
while True:
    content = inp.readline()
    if not content:
        break
    content = content.replace("\n", "")
    content_split = content.split(": ")
    res = int(content_split[0])
    terms_str = content_split[1]
    terms = [int(x) for x in terms_str.split(" ")]
    sum += res if compute(res, terms) else 0
inp.close()

print(sum)
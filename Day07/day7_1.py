# Filename: day7_1.py
# Author: Maxime Zammit
# Created: 2024-12-08
# Description: Equation patcher

def compute(res, terms):
    my_map = [0, 1]
    for term in terms:
        temp_map = []
        for x in my_map:
            temp_map.append(x * term)
            temp_map.append(x + term)
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
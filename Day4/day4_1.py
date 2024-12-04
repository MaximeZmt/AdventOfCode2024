# Filename: day4_1.py
# Author: Maxime Zammit
# Created: 2024-12-04
# Description: Find number of occurrence of XMAS

array = []
lookup = list("XMAS")


def one_way_lookup(i, j, dx, dy) -> int:
    for look in range(len(lookup)):
        if i + dx * look < 0 or j + dy * look < 0 or i + dx * look >= len(array) or j + dy * look >= len(
                array[i + dx * look]) or array[i + dx * look][j + dy * look] != lookup[look]:
            return 0
    return 1


def neighbor_lookup(i, j) -> int:
    count = (one_way_lookup(i, j, -1, -1) + one_way_lookup(i, j, -1, 0) + one_way_lookup(i, j, -1, 1)
             + one_way_lookup(i, j, 0, -1) + one_way_lookup(i, j, 0, 1)
             + one_way_lookup(i, j, 1, -1) + one_way_lookup(i, j, 1, 0) + one_way_lookup(i, j, 1, 1)
             )
    return count


# Input Handling
input = open("input.txt", 'r')
while True:
    content = input.readline()
    if not content:
        break
    split_content = list(content.replace("\n", ""))
    array.append(split_content)
input.close()

total_count = 0
for i in range(len(array)):
    for j in range(len(array[i])):
        if array[i][j] == lookup[0]:
            total_count += neighbor_lookup(i, j)

print(total_count)

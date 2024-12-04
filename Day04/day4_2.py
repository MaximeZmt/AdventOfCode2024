# Filename: day4_2.py
# Author: Maxime Zammit
# Created: 2024-12-04
# Description: find "MAS" pattern in X shape

array = []
lookup = list("MAS")
lookup.sort()


def neighbor_lookup(i, j) -> int:
    if i - 1 < 0 or j - 1 < 0 or i + 1 >= len(array) or j + 1 >= len(array[i - 1]) or j + 1 >= len(array[i + 1]):
        return 0
    comb1 = [array[i - 1][j - 1], "A", array[i + 1][j + 1]]
    comb1.sort()
    comb2 = [array[i - 1][j + 1], "A", array[i + 1][j - 1]]
    comb2.sort()
    val_1 = "".join(comb1)
    val_2 = "".join(comb2)
    ref = "".join(lookup)
    if val_1 == ref and val_2 == ref:
        return 1
    return 0


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
        if array[i][j] == "A":
            total_count += neighbor_lookup(i, j)

print(total_count)

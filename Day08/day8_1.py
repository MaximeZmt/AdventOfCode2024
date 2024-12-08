# Filename: day8_1.py
# Author: Maxime Zammit
# Created: 2024-12-08
# Description: antennas antinode computation v1

from itertools import combinations

def filtering(elem, i_len, j_len):
    if elem[0] < 0 or elem[0] >= i_len or elem[1] < 0 or elem[1] >= j_len:
        return False
    return True
def compute_antinode(store_dict, i_len, j_len):
    final_list = []
    for key in store_dict:
        coords_list = store_dict.get(key, [])
        combi = list(combinations(coords_list, 2))
        for (c1,c2) in combi:
            di = c2[0]-c1[0]
            dj = c2[1]-c1[1]
            final_list.append((c1[0]-di, c1[1]-dj))
            final_list.append((c2[0]+di, c2[1]+dj))

    res = filter(lambda x: filtering(x, i_len, j_len), final_list)
    return list(dict.fromkeys(list(res)))


store_dict = {}
grid = []

i = 0
inp = open("input.txt", 'r')
while True:
    content = inp.readline()
    if not content:
        break
    content = content.replace("\n", "")
    #print(content)
    for j in range(len(content)):
        if not content[j] == ".":
            coord = store_dict.get(content[j], [])
            coord.append((i, j))
            store_dict[content[j]] = coord

    grid.append(list(content))

    i += 1
inp.close()

res = compute_antinode(store_dict, len(grid), len(grid[0]))
#print(res)
print(len(res))

for x in range(len(grid)):
    for xx in range(len(grid)):
        if (x,xx) in res:
            grid[x][xx] = "#"

# for x in grid:
#     print(x)

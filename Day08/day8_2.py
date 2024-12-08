# Filename: day8_2.py
# Author: Maxime Zammit
# Created: 2024-12-08
# Description: ?

from itertools import combinations

def filtering(elem, i_len, j_len):
    if elem[0] < 0 or elem[0] >= i_len or elem[1] < 0 or elem[1] >= j_len:
        return False
    return True
def compute_antinode(store_dict, og_busy, i_len, j_len):
    final_list = []
    for key in store_dict:
        coords_list = store_dict.get(key, [])
        combi = list(combinations(coords_list, 2))
        for (c1,c2) in combi:
            di = c2[0]-c1[0]
            dj = c2[1]-c1[1]
            for mul in range(1, i_len):
                to_add_1 = (c1[0]-(di*mul), c1[1]-(dj*mul))
                to_add_2 = (c2[0]+(di*mul), c2[1]+(dj*mul))
                if to_add_1 not in og_busy:
                    final_list.append(to_add_1)
                if to_add_2 not in og_busy:
                    final_list.append(to_add_2)

    res = filter(lambda x: filtering(x, i_len, j_len), final_list)
    return list(dict.fromkeys(list(res)))


store_dict = {}
og_busy_pos = []
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
            og_busy_pos.append((i, j))

    grid.append(list(content))

    i += 1
inp.close()

res = compute_antinode(store_dict, og_busy_pos, len(grid), len(grid[0]))
#print(res)
print(len(res)+len(og_busy_pos))

# for x in range(len(grid)):
#     for xx in range(len(grid)):
#         if (x,xx) in res:
#             if not grid[x][xx] == ".":
#                 print("ALERT")
#             grid[x][xx] = "#"
#
# for x in grid:
#     print(x)

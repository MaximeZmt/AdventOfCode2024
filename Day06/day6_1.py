# Filename: day6_1.py
# Author: Maxime Zammit
# Created: 2024-12-06
# Description: guard position counter before leaving the grid

map = []

init_pos = (-1, -1)

def do_turn(di, dj):
    if di == -1 and dj == 0:
        return 0, 1
    elif di == 0 and dj == 1:
        return 1, 0
    elif di == 1 and dj == 0:
        return 0, -1
    elif di == 0 and dj == -1:
        return -1, 0

def patrol():
    i_len = len(map)
    j_len = len(map[0])
    cur_pos = init_pos
    di = -1
    dj = 0
    map[cur_pos[0]][cur_pos[1]] = "X"
    distinct_pos = 1
    while True:
        if cur_pos[0]+di >= i_len or cur_pos[1]+dj >= j_len or cur_pos[0]+di < 0 or cur_pos[1]+dj < 0:
            break
        if map[cur_pos[0]+di][cur_pos[1]+dj] == "#":
            di, dj = do_turn(di, dj)
            continue
        else:
            cur_pos = (cur_pos[0] + di, cur_pos[1] + dj)
            if map[cur_pos[0]][cur_pos[1]] == "X":
                continue
            else:
                distinct_pos += 1
                map[cur_pos[0]][cur_pos[1]] = "X"

    return distinct_pos




i = 0
inp = open("input.txt", 'r')
while True:
    content = inp.readline()
    if not content:
        break

    map.append(list(content.replace("\n", "")))
    if init_pos != (-1, -1):
        continue

    for j in range(len(content)):
        if content[j] == "^":
            init_pos = (i, j)
    i += 1
inp.close()


print(init_pos)
print(patrol())

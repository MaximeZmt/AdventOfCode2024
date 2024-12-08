# Filename: day6_2.py
# Author: Maxime Zammit
# Created: 2024-12-06
# Description: Slow and not optimize version of adding blocker counter on the grid
import copy

map = []
dir = [1, 2, 3, 4]
init_pos = (-1, -1)


def do_turn(di, dj):
    if di == -1 and dj == 0:
        return 0, 1, 1
    elif di == 0 and dj == 1:
        return 1, 0, 2
    elif di == 1 and dj == 0:
        return 0, -1, 3
    elif di == 0 and dj == -1:
        return -1, 0, 4


def patrol():
    i_len = len(map)
    j_len = len(map[0])
    cur_pos = init_pos
    di = -1
    dj = 0
    dir_symbol = 4
    map[cur_pos[0]][cur_pos[1]] = "X"
    while True:
        # print("("+str(i)+"-"+str(j)+")\n")
        if cur_pos[0] + di >= i_len or cur_pos[1] + dj >= j_len or cur_pos[0] + di < 0 or cur_pos[1] + dj < 0:
            return False
        if map[cur_pos[0] + di][cur_pos[1] + dj] == "#":
            di, dj, dir_symbol = do_turn(di, dj)
            continue
        else:
            cur_pos = (cur_pos[0] + di, cur_pos[1] + dj)
            if map[cur_pos[0]][cur_pos[1]] == dir_symbol:
                return True
            else:
                map[cur_pos[0]][cur_pos[1]] = dir_symbol
                continue


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

count = 0

copy_map = copy.deepcopy(map)
for i in range(len(map)):
    for j in range(len(map[i])):
        map = copy.deepcopy(copy_map)
        if map[i][j] == "#":
            continue
        elif map[i][j] == "^":
            continue
        else:
            map[i][j] = "#"
            if patrol():
                count += 1

print(count)

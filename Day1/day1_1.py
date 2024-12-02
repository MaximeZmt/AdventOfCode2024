# Filename: day1_1.py
# Author: Maxime Zammit
# Created: 2024-12-02
# Description: Compute pair distance in two lists

def compute_pair_dist(l1, l2):
    return abs(int(l1.pop(0)) - int(l2.pop(0)))


# Init two lists
list1 = []
list2 = []

# Global distance
distance = 0

# Input Handling
input = open("input.txt", 'r')
while True:
    content = input.readline()
    if not content:
        break
    split_content = content.replace("\n", "").split("   ")
    list1.append(split_content[0])
    list2.append(split_content[1])
input.close()

list1.sort()
list2.sort()
while len(list1) > 0 and len(list2) > 0:
    distance += compute_pair_dist(list1, list2)

print(distance)

# Filename: day5_2.py
# Author: Maxime Zammit
# Created: 2024-12-05
# Description: Given some rule of ordering, check if they apply on a list, if not, reorder it according to the rules

import time
from functools import cmp_to_key

start_time = time.time()

parsing_status = 0
rules_set = {}

total_sigma = 0


def custom_comparator(x, y):
    rules_1 = rules_set.get(x, [])
    rules_2 = rules_set.get(y, [])
    if y in rules_1:
        return -1
    elif x in rules_2:
        return 1
    else:
        return 0


key_func = cmp_to_key(custom_comparator)


def do_contradict(computed_slice, rules):
    for x in rules:
        if x in computed_slice:
            return True
    return False


def match_ruleset(li):
    for i in range(len(li)):
        rules = rules_set.get(li[i], [])
        if do_contradict(li[0:i], rules):
            return False
    return True


# Naive Algorithm
# If rules is broken, place the element at the beginning and restart check for order
def do_reorder(li):
    i = 0
    while i < len(li):
        rules = rules_set.get(li[i], [])
        if do_contradict(li[0:i], rules):
            li.insert(0, li.pop(i))
            i = 0
            continue
        i += 1


inp = open("input.txt", 'r')
while True:
    content = inp.readline()
    if not content:
        break

    if parsing_status == 0 and content == "\n":
        parsing_status = 1
        continue

    if parsing_status == 0:
        # Rules set building
        split_content = content.replace("\n", "").split("|")
        content_list = rules_set.get(int(split_content[0]), [])
        content_list.append(int(split_content[1]))
        rules_set[int(split_content[0])] = content_list
    else:
        print_set = content.replace("\n", "").split(",")
        print_set = [int(x) for x in print_set]

        if match_ruleset(print_set):
            continue

        # do reorder
        # do_reorder(print_set)
        print_set.sort(key=key_func)
        mid_print_set = len(print_set) // 2
        total_sigma += print_set[mid_print_set]

inp.close()

print(total_sigma)
print("--- %s seconds ---" % (time.time() - start_time))

# Perf Analysis
# Using do_reorder was roughly 6 seconds
# Using my custom comparator in python sort function, it takes less than 0.01 sec

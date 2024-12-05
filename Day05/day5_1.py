# Filename: day5_1.py
# Author: Maxime Zammit
# Created: 2024-12-05
# Description: Given some rule of ordering, check if they apply on a list

parsing_status = 0
rules_set = {}

total_sigma = 0


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
            mid_print_set = len(print_set) // 2
            total_sigma += print_set[mid_print_set]

inp.close()

print(total_sigma)

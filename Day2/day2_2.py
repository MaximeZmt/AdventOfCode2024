# Filename: day2_2.py
# Author: Maxime Zammit
# Created: 2024-12-02
# Description: Check monotonicity of list of numbers and bound interval difference (allowing delta 1)

# Determine if a list of element is strictly monotonic
def is_strictly_monotonic(list):
    prev = None
    is_ascending = None
    for i in range(len(list)):
        # if not first elem of list
        if prev is not None:
            # if second elem, determine gradient
            if is_ascending is None:
                if list[i] > prev:
                    is_ascending = True
                    prev = list[i]
                    continue
                elif list[i] < prev:
                    is_ascending = False
                    prev = list[i]
                    continue

            # check if break strictly monotonic
            if is_ascending:
                if list[i] <= prev:
                    return i
            else:
                if list[i] >= prev:
                    return i
        prev = list[i]
    return None


def diff_bound(list, min, max):
    prev = None
    for i in range(len(list)):
        if prev is not None:
            if not (min <= abs(list[i] - prev) <= max):
                return i
        prev = list[i]
    return None


def is_safe(og_list):
    li = og_list.copy()
    is_strictly_monotonic_res = is_strictly_monotonic(li)
    is_diff_bound_res = diff_bound(li, 1, 3)
    print(og_list)
    print(is_diff_bound_res)
    print(is_strictly_monotonic_res)
    if is_strictly_monotonic_res is None and is_diff_bound_res is None:
        return True
    if is_strictly_monotonic_res is not None:
        li = og_list.copy()
        li.pop(is_strictly_monotonic_res)
        if is_strictly_monotonic(li) is None and diff_bound(li, 1, 3) is None:
            return True
        li = og_list.copy()
        li.pop(is_strictly_monotonic_res-1)
        if is_strictly_monotonic(li) is None and diff_bound(li, 1, 3) is None:
            return True
    if is_diff_bound_res is not None:
        li = og_list.copy()
        li.pop(is_diff_bound_res)
        if is_strictly_monotonic(li) is None and diff_bound(li, 1, 3) is None:
            return True
    li = og_list.copy()
    li.pop(0)
    if is_strictly_monotonic(li) is None and diff_bound(li, 1, 3) is None:
        return True
    else:
        print("NOPE")
        return False


safe_reports = 0

# Input Handling
input = open("input.txt", 'r')
while True:
    content = input.readline()
    if not content:
        break
    report_levels_str = content.replace("\n", "").split(" ")
    report_levels = [int(i) for i in report_levels_str]
    safe_reports += 1 if is_safe(report_levels) else 0
input.close()

print(safe_reports)
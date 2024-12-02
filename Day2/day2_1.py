# Filename: day2_1.py
# Author: Maxime Zammit
# Created: 2024-12-02
# Description: Check monotonicity of list of numbers and bound interval difference

# Determine if a list of element is strictly monotonic
def is_strictly_monotonic(list):
    prev = None
    is_ascending = None
    for i in list:
        # if not first elem of list
        if prev is not None:
            # if second elem, determine gradient
            if is_ascending is None:
                if i > prev:
                    is_ascending = True
                    prev = i
                    continue
                elif i < prev:
                    is_ascending = False
                    prev = i
                    continue

            # check if break strictly monotonic
            if is_ascending:
                if i <= prev:
                    return False
            else:
                if i >= prev:
                    return False
        prev = i
    return True


def diff_bound(list, min, max):
    prev = None
    for i in list:
        if prev is not None:
            if not (min <= abs(i - prev) <= max):
                return False
        prev = i
    return True


def is_safe(list):
    return is_strictly_monotonic(list) and diff_bound(list, 1, 3)


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
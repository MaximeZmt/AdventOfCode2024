# Filename: day3_2.py
# Author: Maxime Zammit
# Created: 2024-12-03
# Description: Tokenization of mul(x,y) with x, y two numbers of 1 to 3 digits that are not disabled with don't

# Import module
import re

# Var init
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
result = 0
# here we use the non-greedy match to capture the smallest as possible sequence of don't() ... do() in order to
# simulate a sequential reading
pattern_disable = r"don't\(\).*?do\(\)"

# Input Handling
input = open("input.txt", 'r')
lines = input.readlines()
content = "".join(lines)
input.close()

# Using the flags re.DOTALL to avoid issue if new line when parsing the input. Ignore them.
content_without_disable = re.sub(pattern_disable, "", content, flags=re.DOTALL)

regex_matches = re.findall(pattern, content_without_disable)

for x,y in regex_matches:
    result += int(x)*int(y)

print(result)
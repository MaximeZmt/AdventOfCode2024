# Filename: day3_1.py
# Author: Maxime Zammit
# Created: 2024-12-03
# Description: Tokenization of mul(x,y) with x, y two numbers of 1 to 3 digits

# Import module
import re

# Var init
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
result = 0

# Input Handling
input = open("input.txt", 'r')
lines = input.readlines()
content = "".join(lines)
input.close()

regex_matches = re.findall(pattern, content)

for x,y in regex_matches:
    result += int(x)*int(y)

print(result)
# Filename: day1_2.py
# Author: Maxime Zammit
# Created: 2024-12-02
# Description: Computation of similarity score between two lists

# Init two lists
list1 = []
list2 = []

# Global distance
similarity_score = 0

# Input Handling
input = open("input.txt", 'r')
while True:
	content = input.readline()
	if not content:
		break
	split_content = content.replace("\n","").split("   ")
	list1.append(split_content[0])
	list2.append(split_content[1])
input.close()


for i in list1:
	similarity_score += int(i)*list2.count(i)

print(similarity_score)

import numpy as np

current_line = 719
number = 0
nums = []

html_file = open("sync.html")
for line in html_file:
    number = number + 1
    if number == current_line:
        current_line = current_line + 712
        current_num = line
        current_num = current_num[10:].strip()
        current_num = current_num[:-5].strip()
        nums.append(int(current_num))

numsp = np.array(nums)

print(numsp)
import re

fh = open('regex_sum_268202.txt')
summation = 0
count = 0
for line in fh:
    nums = re.findall('[0-9]+',line)
    count += len(nums)
    temp = 0
    for number in nums:
        temp += int(number)
    summation += temp
print summation
print count

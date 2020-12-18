import collections

f = open("input.txt", "r")

valid_count = 0
# Part 1 Solution
# for line in f:
#     rule, password = line.split(':')
#     _range, letter = rule.split(' ')
#     _min, _max = map(lambda x : int(x), _range.split('-'))
#     password = password.strip()

#     counts = collections.Counter(password)
#     if counts[letter] >= _min and counts[letter] <= _max:
#         valid_count += 1

# Part 2 Solution
for line in f:
    rule, password = line.split(':')
    _range, letter = rule.split(' ')
    i, j = map(lambda x : int(x), _range.split('-'))
    password = password.strip()

    if len(password) < i or len(password) < j:
        continue

    if (password[i-1] == letter) ^ (password[j-1] == letter):
        valid_count += 1

print(valid_count)
f.close()

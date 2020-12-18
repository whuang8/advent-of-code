file = open("input.txt", "r")
# file = open("input2.txt", "r")

required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
fields = set()
valid_passports = 0

for line in file:
    line = line.strip('\n')
    if len(line) == 0:
        if required_fields - fields == set() or required_fields - fields == {'cid'}:
            valid_passports += 1
        fields = set()
        continue
    fs = list(map(lambda field: field.split(":")[0], line.split(" "))) 
    for f in fs:
        fields.add(f)
if required_fields - fields == set() or required_fields - fields == {'cid'}:
    valid_passports += 1

print(valid_passports)
file.close()

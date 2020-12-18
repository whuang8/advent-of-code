import sys

f = open(sys.argv[1], "r")
seen = dict()

for num in f:
    seen.add(int(num))
f.close()

for num1 in seen:
    complement1 = 2020 - num1
    for num2 in seen:
        complement2 = complement1 - num2
        if complement2 in seen:
            print(num1 * num2 * complement2)
            exit()

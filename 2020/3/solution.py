from functools import reduce

f = open("input.txt", "r")
# f = open("input2.txt", "r")
matrix = [list(line)[:-1] for line in f]
f.close()

width = len(matrix[0])
height = len(matrix)
trees_encountered = []
slopes = [
    (1,1),
    (3,1),
    (5,1),
    (7,1),
    (1,2),
]

for slope in slopes:
    i, j, trees = slope[1], slope[0], 0
    while i < height:
        if j >= width:
            j = j - width
        if matrix[i][j] == '#':
            trees += 1
        j += slope[0]
        i += slope[1]
    trees_encountered.append(trees)

print(reduce(lambda x, y: x*y, trees_encountered))


floor = 0

with open('input.txt') as f:
    for line in f:
        floor += line.count('(') - line.count(')')

print(floor)
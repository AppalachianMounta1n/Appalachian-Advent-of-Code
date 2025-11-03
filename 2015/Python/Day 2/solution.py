presentDimensions = []
surfaceArea = 0

with open("input.txt") as f:
    for line in f :
        presentDimensions.append(line)

for i in presentDimensions:
    dimensions = i.split("x")
    surfaceArea += (2 * (int(dimensions[0]) * int(dimensions[1])) + 2 * (int(dimensions[1]) * int(dimensions[2])) + 2 * (int(dimensions[2]) * int(dimensions[0]))) + min([int(dimensions[0]) * int(dimensions[1]), int(dimensions[1]) * int(dimensions[2]), int(dimensions[2]) * int(dimensions[0])])
    dimensions = []

print(surfaceArea)
startingLocation = (0,0)
santaHistory = [startingLocation]
roboHistory = [startingLocation]

with open("input.txt") as f:
    directions = list(f.read())

for i, v in enumerate(directions):
    if i % 2 == 0:
        if v == "^":
            santaHistory.append((santaHistory[-1][0], santaHistory[-1][1] + 1))
        elif v == "v":
            santaHistory.append((santaHistory[-1][0], santaHistory[-1][1] - 1))
        elif v == ">":
            santaHistory.append((santaHistory[-1][0] + 1, santaHistory[-1][1]))
        elif v == "<":
            santaHistory.append((santaHistory[-1][0] - 1, santaHistory[-1][1]))
    else:
        if v == "^":
            roboHistory.append((roboHistory[-1][0], roboHistory[-1][1] + 1))
        elif v == "v":
            roboHistory.append((roboHistory[-1][0], roboHistory[-1][1] - 1))
        elif v == ">":
            roboHistory.append((roboHistory[-1][0] + 1, roboHistory[-1][1]))
        elif v == "<":
            roboHistory.append((roboHistory[-1][0] - 1, roboHistory[-1][1]))

print("Santa Presents Delivered: ", len(set(santaHistory)))
print("Robot Presents Delivered: ", len(set(roboHistory)))
print("Total Presents Delivered: ", len(set(santaHistory).union(set(roboHistory))))
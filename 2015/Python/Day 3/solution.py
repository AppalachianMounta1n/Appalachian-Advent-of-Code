startingLocation = (0,0)
history = [startingLocation]

with open("input.txt") as f:
    directions = f.read()

for i in directions:
    if i == "^":
        history.append((history[-1][0], history[-1][1] + 1))
    elif i == "v":
        history.append((history[-1][0], history[-1][1] - 1))
    elif i == ">":
        history.append((history[-1][0] + 1, history[-1][1]))
    elif i == "<":
        history.append((history[-1][0] - 1, history[-1][1]))

print(len(set(history)))
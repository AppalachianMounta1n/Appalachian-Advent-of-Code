floor = 0
instructions = ""

with open('input.txt') as f:
    for line in f:
        instructions += line
        
    floor += instructions.count('(') - instructions.count(')')
    print(floor)

    floor = 0
    basementFirst = 0
    for i in instructions:
        floor += 1 if i == '(' else -1
        basementFirst -= -1
        if floor == -1:
            print("First basement: " + str(basementFirst))
            break
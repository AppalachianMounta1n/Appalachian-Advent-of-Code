import re
from collections import Counter

with open("input.txt") as f:
    lines = [line.rstrip() for line in f]

niceCountOne = 0
niceCountTwo = 0

def vowelCount(line, nice):
    vowelList = ["a", "e", "i", "o", "u"]
    vowels = sum(1 for c in line if c in vowelList) #https://stackoverflow.com/questions/2600191/how-do-i-count-the-occurrences-of-a-list-item, #https://www.w3schools.com/PYTHON/ref_list_count.asp

    if vowels >= 3:
        nice += 1

    return nice

def repeatCount(line, nice):
    #if len(set(line)) != len(line): #https://stackoverflow.com/questions/32090058/testing-whether-a-string-has-repeated-characters
    #    nice += 1

    lastChar = None
    repeat = Counter()
    for i, char in enumerate(line): #https://www.quora.com/How-do-you-find-consecutive-repeated-characters-in-a-string-1
        if char == lastChar:
            repeat[char] += 1
        lastChar = char

    if repeat:
        nice += 1

    return nice

def stringHunt(line, nice):
    invalidStrings = ["ab", "cd", "pq", "xy"]
    
    if not any([x in line for x in invalidStrings]): #https://stackoverflow.com/questions/32121521/in-python-how-can-i-check-that-a-string-does-not-contain-any-string-from-a-list
        nice += 1

    return nice

def pairHunt(line, nice):
    if bool(re.search(r'(..).*\1', line)): #https://mimo.org/glossary/python/regex-regular-expressions
        nice += 1

    return nice

def repeatBetween(line, nice):
    if bool(re.search(r'([a-zA-Z]).\1', line)):
        nice += 1

    return nice

for i in lines:
    nice = vowelCount(i, 0)
    nice = repeatCount(i, nice)
    nice = stringHunt(i, nice)

    if nice == 3:
        niceCountOne += 1

for i in lines:
    nice = pairHunt(i, 0)
    nice = repeatBetween(i, nice)

    if nice == 2:
        niceCountTwo += 1

print("Nice strings by initial ruleset: ", niceCountOne)
print("Nice strings by second ruleset: ", niceCountTwo)
import random

firstWord = input()
i = len(firstWord)
q = list(firstWord)
res = ""
while i > 0:
    res = res + random.choice(q)
    i -= 1
print(res)

# -*- coding: utf-8 -*-


z = []

for x in range(10):
    z.append(x)

print(z)

z = []

for x in range(10):
    for y in range(6):
        z.append([x,y])
print(z)

z = [[x,y] for y in range(10) for x in range(6)]
print(z)



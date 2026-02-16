from math import ceil, log10
from random import randint

sc = 0

# Tile merging and shifting logic simplified
def p(typ, i, k):
    if typ == 1:
        # Move right logic (row 0, 1, 2, 3)
        for idx in range(i, 0, -4):
            if k[idx] == 0:
                k[idx] = k[idx - 4]
                k[idx - 4] = 0
    elif typ == 2:
        # Move down logic (column 0, 4, 8, 12)
        for idx in range(i, 4):
            if k[idx] == 0:
                k[idx] = k[idx - 4]
                k[idx - 4] = 0
    elif typ == 3:
        # Move up logic (column 0, 4, 8, 12)
        for idx in range(i, 4):
            if k[idx] == 0:
                k[idx] = k[idx + 4]
                k[idx + 4] = 0
    elif typ == 4:
        # Move left logic (row 0, 1, 2, 3)
        for idx in range(i, 4):
            if k[idx] == 0:
                k[idx] = k[idx + 4]
                k[idx + 4] = 0
    return k

def q():
    return str(sc) if sc < 100000 else f"2^{int(log10(sc+1))}"

def a(b):
    return "    " if b == 0 else "2^" + str(b) if b >= 14 else str(2**b).rjust(4)

def c(d):
    f = "+----" * 4 + "+"
    for row in d:
        f += "\n|" + "|".join([a(cell) for cell in row]) + "|"
    f += f"\n+----score:{q()}----+\ndirection:"
    return int(input(f)) // 2 - 1

def g(h):
    return [[a(h[i*4+j]) for j in range(4)] for i in range(4)]

def m():
    return randint(0, 15)

k = [0] * 16

while True:
    www = 0
    while True:
        www += 1
        if www == 80:
            raise Exception("lol u lose")
        n = m()
        if k[n] == 0:
            k[n] = 1
            break
    o = c(g(k))
    if o == 0:
        for i in [0, 1, 2, 3]:
            k = p(1, i, k)
            if k[12 + i] == k[8 + i] and k[8 + i]:
                sc += 2 ** k[12 + i]
                k[12 + i] += 1
                k[8 + i] = 0
            if k[4 + i] == k[8 + i] and k[4 + i]:
                sc += 2 ** k[8 + i]
                k[8 + i] += 1
                k[4 + i] = 0
            if k[i] == k[4 + i] and k[i]:
                sc += 2 ** k[4 + i]
                k[4 + i] += 1
                k[i] = 0
            k = p(1, i, k)
    elif o == 1:
        for i in [0, 4, 8, 12]:
            k = p(2, i, k)
            if k[i] == k[1 + i] and k[1 + i]:
                sc += 2 ** k[i]
                k[i] += 1
                k[1 + i] = 0
            if k[2 + i] == k[1 + i] and k[2 + i]:
                sc += 2 ** k[1 + i]
                k[1 + i] += 1
                k[2 + i] = 0
            if k[3 + i] == k[2 + i] and k[3 + i]:
                sc += 2 ** k[2 + i]
                k[2 + i] += 1
                k[3 + i] = 0
            k = p(2, i, k)
    elif o == 2:
        for i in [0, 1, 2, 3]:
            k = p(3, i, k)
            if k[i] == k[4 + i] and k[i]:
                sc += 2 ** k[i]
                k[i] += 1
                k[4 + i] = 0
            if k[8 + i] == k[4 + i] and k[8 + i]:
                sc += 2 ** k[4 + i]
                k[4 + i] += 1
                k[8 + i] = 0
            if k[12 + i] == k[8 + i] and k[12 + i]:
                sc += 2 ** k[8 + i]
                k[8 + i] += 1
                k[12 + i] = 0
            k = p(3, i, k)
    elif o == 3:
        for i in [0, 4, 8, 12]:
            k = p(4, i, k)
            if k[3 + i] == k[2 + i] and k[2 + i]:
                sc += 2 ** k[3 + i]
                k[3 + i] += 1
                k[2 + i] = 0
            if k[1 + i] == k[2 + i] and k[1 + i]:
                sc += 2 ** k[2 + i]
                k[2 + i] += 1
                k[1 + i] = 0
            if k[i] == k[1 + i] and k[i]:
                sc += 2 ** k[1 + i]
                k[1 + i] += 1
                k[i] = 0
            k = p(4, i, k)

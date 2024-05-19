L = [15, 24, 'abc', 9]
for i in L:
    while i < len(L):
        L.insert(i, 0)
        i += 2
    print(L)

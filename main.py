def test():
    L = [1, 2, 3, 4]
    L1 = L
    L2 = L[:]
    L1[1] = 18
    L2[2] = 20
    print(L)
    print(L1)
    print(L2)


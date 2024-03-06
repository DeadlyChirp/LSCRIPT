def test():
    L=[1,2,3,4]
    L1=L
    L2=L[:]
    L1[1]=18
    L2[2]=20
    print(L)
    print(L1)
    print(L2)

test()


# on L1 = L on referencie la liste L dans L1 et puis on recopie L a L2
#L1[1], on remplace la premiere valeur donc 1 a 18
#vu que L1 est referiencie a L donc tous les changements s'effectuent dans la liste L et L1

#les changements de L2 n'effectue pas sur la liste L2 car les 2 sont independants. On a fait une copie coller
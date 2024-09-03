def parittoimienpoistaja (lista):
    parilliset = []
    for i in lista:
        if i % 2 == 0:
            parilliset.append(i)

    return parilliset
randlista = [1,4,6,3,13,12,20,22,21,67,6,7]
parillisetlista =  parittoimienpoistaja(randlista)
print(parillisetlista)


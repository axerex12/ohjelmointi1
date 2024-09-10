nimi = "jane doe"
namelist = []
while nimi !="":
    nimi=(input("anna nimi: "))
    if nimi in namelist:
        print("Aiemmin syötetty nimi")
    else:
        print("Uusi nimi")
        namelist.append(nimi)


for i in namelist:
    print(i)


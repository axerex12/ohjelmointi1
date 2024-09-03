while True:
    alkuluku = int(input("Anna alkuluku!: "))
    if alkuluku % 1 == 0 and alkuluku % alkuluku == 0:
        laskuri = 0
        for i in range(alkuluku - 1, 1, -1):
            if alkuluku % i == 0:
                print("ei ole alkuluku")
                laskuri += 1
                break
        if laskuri == 0:
            print("Alkuluku")



    else:
        print("Ei ole alkuluku!")










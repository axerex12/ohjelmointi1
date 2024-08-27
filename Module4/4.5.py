käyttis = "python"
salasana = "rules"
i =0
while 1 < 2:
    annettukäyttis=input("Anna käyttäjätunnus!: ")
    annettusalasana = input("Anna salasana!: ")
    if käyttis != annettukäyttis or salasana != annettusalasana:
        i +=1
        if i == 5:
            print("Pääsy evätty")
            break
    else:
        print("Tervetuloa!")


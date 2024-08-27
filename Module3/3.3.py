sukupuoli=input("ANNA BIOLOGINEN SUKUPUOLESI! nainen/mies")
hemeglov = int(input("ANNA HOMOGLEBIINI ARVO!"))

if sukupuoli == "mies":
    if hemeglov >= 134 and hemeglov < 196:
        print("hemoglobiiniarvo on normaali")
    elif hemeglov < 134:
        print("hemoglobiiniarvo on vähäinen")
    elif hemeglov > 195:
        print("hemoglobiiniarvo on liian iso")
elif sukupuoli == "nainen":
    if hemeglov >= 117 and hemeglov <= 175:
        print("hemoglobiiniarvo on normaali")
    elif hemeglov < 117:
        print("hemoglobiiniarvo on vähäinen")
    elif hemeglov > 175:
        print("hemoglobiiniarvo on liian iso")





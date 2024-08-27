hyttiluokka =input()

if hyttiluokka == "A" or hyttiluokka == "B" or hyttiluokka == "C" or hyttiluokka == "LUX":
    if hyttiluokka == "LUX":
        print("LUX on parvekkeellinen hytti yläkannella.")
    if hyttiluokka == "A":
        print("A on ikkunallinen hytti autokannen yläpuolella.")
    if hyttiluokka == "B":
        print("B on ikkunaton hytti autokannen yläpuolella.")
    if hyttiluokka == "C":
        print("C on ikkunaton hytti autokannen alapuolella.")

else:
    print("Virheellinen hyttiluokka")
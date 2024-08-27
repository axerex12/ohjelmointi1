leiviskät=float(input())
naulat=float(input())
luodit=float(input())
kilot=0

leiviskägramma=leiviskät*20*32*13.3
naulagramma= naulat*32*13.3
luotigramma= luodit*13.3

yhteensägrammat=leiviskägramma+naulagramma+luotigramma

while yhteensägrammat>1000:
    yhteensägrammat-=1000
    kilot+=1

print("Massa nykymittojen mukaan: ")
print(f"{kilot} kilogrammaa ja {yhteensägrammat: 2.2f} grammaa.")

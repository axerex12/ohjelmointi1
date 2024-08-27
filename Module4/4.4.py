import random

while True:
   arvaus = int(input("Anna numero 1-10!: "))
   randnumero =(random.randint(0, 11))
   if arvaus == randnumero:
       print("Oikein!")
       break
   elif arvaus < randnumero:
       print ("liian pieni arvaus!")
   elif arvaus > randnumero:
       print("liian iso arvaus!")
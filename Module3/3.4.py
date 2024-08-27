vuosi=int(input("Anna syntymä vuuotesi: "))

if vuosi % 4 == 0:
    print("Sinun vuotesi on karkaus vuosi!")
elif vuosi % 100 == 0 and vuosi % 400 == 0:
    print("Sinun vuotesi on karkaus vuosi!")
else:
    print("ei ole karkaus vuosi")
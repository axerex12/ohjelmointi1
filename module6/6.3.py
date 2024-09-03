def galoonalitroiksi(galoonat):
    litroina = galoonat * 3.785
    return litroina


galoonamount = float(input("Anna galoona määrä bensaa!: "))
litroina = galoonalitroiksi(galoonamount)

print (round(litroina,2))



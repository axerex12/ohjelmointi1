import random
list3=[]
list4=[]
counter1=0
counter2=0

while counter1!=3:
    counter1+=1
    list3.append(random.randint(0, 9))
while counter2!=4:
    counter2+=1
    list4.append(random.randint(1, 6))


print(f"Kolme numeroinen koodi: {list3}")
print(f"Neljä numeroinen koodi: {list4}")
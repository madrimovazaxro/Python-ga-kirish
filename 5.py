import os
os.system("cls")

son = int(input("Son: "))
birlar = son % 10 #3
onlar = son//10 % 10 #2
yuzlar = son // 100

print("Teskari son: ", birlar*100 + onlar*10+ yuzlar)

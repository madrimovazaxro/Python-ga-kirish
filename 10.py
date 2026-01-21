import os
os.system("cls")

son = int(input("Son: "))
birlar = son % 10
onlar = son // 10 % 10
yuzlar = son // 100 % 10
minglar = son // 1000
print("MAX: ", max(birlar, onlar, yuzlar, minglar))
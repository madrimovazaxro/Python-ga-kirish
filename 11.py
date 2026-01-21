import os
os.system("cls")

son = int(input("Son: "))
birlar = son%10
onlar = son//10 % 10
yuzlar = son // 100
print("Natija: ", yuzlar*10+birlar)
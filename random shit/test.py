rezultat = 0
vsota_stevk = 0

for i in range(1, 99999):
    str1 = str(i)
    str1.split()
    for a in str1:
        vsota_stevk += int(a)

    if vsota_stevk % 9 == 0 or vsota_stevk % 5 == 0:
        rezultat += 1
    vsota_stevk = 0

print(rezultat)


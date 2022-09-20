bawah = 900
atas = 1000
for angka in range(bawah, atas + 1, 1):
    prima = True
    for x in range(2, angka - 1 + 1, 1):
        if angka % x == 0:
            prima = False
    if prima == True:
        print(angka)

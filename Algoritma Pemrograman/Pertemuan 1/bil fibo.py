# batas atas = 200 diberi karena jumlah deret fibonacii =/= (tidak sama dengan) nilai dari deret fibonacci
atas = 200
fibo = [0] * (atas)

# dibuat list bil bulat sekaligus fungsi
for angka in range(0, 20 + 1, 1):
    if angka == 0:
        fibo[angka] = 1
        
        # fibonacci yang diminta dari soal dimulai dari 1
    else:
        if angka == 1:
            fibo[angka] = angka
        else:
            fibo[angka] = fibo[angka - 2] + fibo[angka - 1]
    if fibo[angka] > 200:
        exit()
        # ketika nilai lebih dari 200 maka program akan berhenti
    else:
        print(fibo[angka])

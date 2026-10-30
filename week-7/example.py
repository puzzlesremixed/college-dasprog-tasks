balance  = 500000

print(f"Selamat datang! Saldo anda saat ini adalah: Rp{balance}")

while True:
    try:
        payment: int = int(input("Jumlah pembelian: "))
        if 0 < payment:
            break
        else:
            print("ERROR : Mohon masukkan angka diatas 0.")
            print("----------------------------")
    except ValueError:
        print("ERROR : Mohon masukkan angka yang valid!")
        print("----------------------------")


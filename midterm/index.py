daftarHarga = (100000, 300000)
batasReservasi = (2, 5)
listReservasi = [0, 0]
batasDiskon = 5
persenDiskon = 5 / 100


def main():
    # Seleksi kamar
    while True:
        try:
            print("Pilih kamar:")
            print(f"1. Reguler (Sisa kamar: {batasReservasi[0] - listReservasi[0]})")
            print(f"2. VIP (Sisa kamar: {batasReservasi[1] - listReservasi[1]})")
            
            jenisKamar = int(input("Masukkan nomor kamar: ")) - 1
            if 0 < jenisKamar+1 <= 2:
                break
            else:
                print("----------------------------")
                print("ERROR : Mohon masukkan angka antara 1 hingga 2.")
                print("----------------------------")
        except ValueError:
            print("----------------------------")
            print("ERROR : Mohon masukkan angka yang valid!")
            print("----------------------------")
    
    if (batasReservasi[jenisKamar] > listReservasi[jenisKamar]):
        listReservasi[jenisKamar] += 1
    else:
        print("----------------------------")
        print("PERINGATAN : Kamar penuh! Mohon pilih kelas lain.")
        print("----------------------------")
        return

    while True:
        try:
            durasi = int(input("Lama menginap dalam hari: "))
            if 0 < durasi <= 99:
                break
            else:
                print("----------------------------")
                print("ERROR : Mohon masukkan angka antara 1 hingga 99.")
                print("----------------------------")
        except ValueError:
            print("----------------------------")
            print("ERROR : Mohon masukkan angka yang valid!")
            print("----------------------------")
    

    hargaKamar = daftarHarga[jenisKamar]
    totalHargaAwal = hargaKamar * durasi
    hargaAkhir = totalHargaAwal
    
    print("----------------------------")
    if durasi >= batasDiskon:
        print(f"Anda mendapat diskon!")
        hargaAkhir = totalHargaAwal - (totalHargaAwal * persenDiskon)
        
    print(f"Total akhir: Rp{round(hargaAkhir):,}".replace(",", "."))
    print(f"Sisa kamar: {batasReservasi[jenisKamar] - listReservasi[jenisKamar]}")
    print("----------------------------")
    # Sisa


while True:
    main()

DAFTAR_HARGA = (100000, 300000)
BATAS_RESERVASI = (2, 5)
LIST_RESERVASI = [0, 0]
BATAS_DISKON = 5
PERSEN_DISKON = 0.05
NAMA_KAMAR = ("Reguler", "VIP")
SEPARATOR = "-" * 24


def main():
    while True:
        try:
            # Seleksi kamar
            print("Pilih kamar:")
            for i in range(len(DAFTAR_HARGA)):
                sisa = BATAS_RESERVASI[i] - LIST_RESERVASI[i]
                print(f"{i + 1}. {NAMA_KAMAR[i]} (Sisa kamar: {sisa})")

            jenis_kamar = int(input("Masukkan nomor kamar (1-2): "))
            if 1 <= jenis_kamar <= 2:
                idx = jenis_kamar - 1
                break
            else:
                print(SEPARATOR)
                print("ERROR : Mohon masukkan angka antara 1 hingga 2.")
                print(SEPARATOR)
        except ValueError:
            print(SEPARATOR)
            print("ERROR : Mohon masukkan angka yang valid!")
            print(SEPARATOR)

    # Cek ketersediaan kamar
    if LIST_RESERVASI[idx] < BATAS_RESERVASI[idx]:
        LIST_RESERVASI[idx] += 1
    else:
        print(SEPARATOR)
        print("PERINGATAN : Kamar penuh! Mohon pilih kelas lain.")
        print(SEPARATOR)
        return

    # Input durasi menginap
    while True:
        try:
            durasi = int(input("Lama menginap dalam hari (1-99): "))
            if 1 <= durasi <= 99:
                break
            else:
                print(SEPARATOR)
                print("ERROR : Mohon masukkan angka antara 1 hingga 99.")
                print(SEPARATOR)
        except ValueError:
            print(SEPARATOR)
            print("ERROR : Mohon masukkan angka yang valid!")
            print(SEPARATOR)

    # Perhitungan harga
    harga_kamar = DAFTAR_HARGA[idx]
    total_harga_awal = harga_kamar * durasi
    harga_akhir = total_harga_awal

    print(SEPARATOR)
    if durasi >= BATAS_DISKON:
        print("Anda mendapat diskon 5%!")
        harga_akhir = total_harga_awal * (1 - PERSEN_DISKON)

    formatted_harga = f"Rp{round(harga_akhir):,}".replace(",", ".")
    print(f"Total akhir: {formatted_harga}")
    print(f"Sisa kamar {NAMA_KAMAR[idx]}: {BATAS_RESERVASI[idx] - LIST_RESERVASI[idx]}")
    print(SEPARATOR)


# main program loop
while True:
    main()
    lanjut = input("Ingin melakukan reservasi lagi? (y/n): ").strip().lower()
    if lanjut != 'y':
        print("Terima kasih telah menggunakan sistem reservasi!")
        break

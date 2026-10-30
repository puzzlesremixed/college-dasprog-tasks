total = int(input("Total belanja: "))
status = input("Member? (y/t): ")
uang = int(input("Uang dibayar: "))

punya_member = status == "y"

if total > 500000:
    persen = 10
elif total > 200000:
    persen = 5
else:
    persen = 0

diskon = total * persen / 100
total_bayar = total - diskon

if punya_member:
    if total >= 100000:
        print("Dapat voucher Rp10.000 untuk kunjungan berikutnya")
    else:
        print("Belanja lebih agar dapat voucher")
else:
    print("Daftar member untuk dapat voucher")

if uang >= total_bayar:
    kembalian = uang - total_bayar
    bayar = f"Rp{round(total_bayar):,}".replace(",","")
    balik = f"Rp{round(kembalian):,}".replace(",",".")
    print(f"Bayar: {bayar} | Kembalian: {balik}")
else:
    kurang = total_bayar - uang
    print(f"Uang kurang Rp{round(kurang):,}".replace(",","."))


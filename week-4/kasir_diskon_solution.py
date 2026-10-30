jumlah = int(input("Jumlah beli: "))
total = int(input("Total belanja: "))

if jumlah <= 0:
    print("Jumlah tidak valid")
else:
    if total > 500000:
        persen = 10
    elif total > 200000:
        persen = 5
    else:
        persen = 0
    
    diskon = total * persen / 100
    total_bayar = total - diskon
    
    if persen > 0:
        print(f"Diskon {persen}%, hemat Rp{round(diskon):,}".replace(",", "."))
    else:
        print("Tidak ada diskon")
        
    print(f"Total bayar: Rp{round(total_bayar):,}".replace(",", "."))
    

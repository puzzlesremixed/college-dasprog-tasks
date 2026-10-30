total = int(input("Total belanja: ")) 
if total > 500000: 
    persen = 10 
elif total > 200000:
    persen = 5
else:
    persen = 0

diskon = total * persen / 100
total_bayar = total - diskon
print(f"Bayar: Rp{round(total_bayar):,}".replace(",","."))

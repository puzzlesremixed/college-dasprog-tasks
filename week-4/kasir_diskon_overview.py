# harga = int(input("Harga barang: "))
jumlah = int(input("Jumlah belanja: "))
total = int(input("Total belanja: "))

print("--------------------")
if jumlah <= 0:
    print("Mohon masukkan jumlah yang valid!")
else :     
    disc_percentage = 0
    percentage_value = 0  
    # 10% jika total > Rp500.000
    if total > 500000:
        percentage_value =  10
        disc_percentage = percentage_value  / 100
    # 5% jika total > Rp200.000
    elif total > 200000:
        percentage_value = 5
        disc_percentage = percentage_value / 100
    
    print(f"Anda mendapatkan diskon {percentage_value}%!")
    discount = total * disc_percentage
    
    final_price = total - discount
    
    if discount > 0:
        print(f"Total diskon: Rp{round(discount)}")
        print(f"Total belanja sebelum diskon: Rp{round(total)}")
    else:
        print("Anda tidak mendapat diskon.")
        
    print("--------------------")
    print(f"Total belanja akhir: Rp{round(final_price)}")
    print("--------------------")
    

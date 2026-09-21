barang1 = int(input("Harga barang 1: ")) 
total += barang1
print(f"Subtotal: Rp{total:,}".replace(",", "."))

barang2 = int(input("Harga barang 2: ")) 
total += barang2
print(f"Subtotal: Rp{total:,}".replace(",", "."))

barang3 = int(input("Harga barang 3: ")) 
total += barang3
print(f"Total	: Rp{total:,}".replace(",", "."))

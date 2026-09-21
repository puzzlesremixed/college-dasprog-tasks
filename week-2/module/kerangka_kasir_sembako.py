# input: Tanya berapa banyak barang yang dibeli
products_number = input("Berapa banyak: ")

# process: buat object product dan array untuk menampung barang yang dibeli nanti
# process: Loop setiap barang yang dibeli
# input: tanyakan harga per barang
name = input("Nama barang: ") 
price = int(input("Harga: "))
qty = int(input("Kelipatan barang: "))
# process : buat object product dan masukkan ke array

# process : loop unuk menampilkan detail belanja per produk
# output: tampilkan detail belanja per produk 
print(f"{product.name} (Rp{product.price})")
print(f"x{product.qty} (Rp{current_total})")
print("----------------------------")
# process: hitung total belanja
# output: tampilkan total belanja
print("Total belanja: Rp69.000")
print("----------------------------")
# process: tentukan diskon jika total belanja lebih dari 200.000
# output: tampilkan total belanja setelah diskon jika ada
print("Diskon 5%: -Rp67.000")
print("Total setelah diskon: Rp67.000")
print("----------------------------")
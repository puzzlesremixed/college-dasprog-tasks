
# MASUKAN
nama1 = input("Nama barang 1: ") 
harga1 = int(input("Harga barang 1: ")) 

nama2 = input("Nama barang 2: ") 
harga2 = int(input("Harga barang 2: ")) 

nama3 = input("Nama barang 3: ") 
harga3 = int(input("Harga barang 3: ")) 

# PROSES
total = harga1 + harga2 + harga3

# PROSES: cek apakah total > 200000, jika ya diskon 5% 
# (belum bisa ditulis — butuh if, dipelajari Minggu 4) 
# total_bayar = ...

# KELUARAN
rupiah_total = f"Rp{total:,}".replace(",", ".") 
print(f"Total belanja: {rupiah_total}")
# print(f"Total bayar : ...") 
# setelah diskon, Minggu 4

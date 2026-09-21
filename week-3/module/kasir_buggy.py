# Program kasir — ada DUA bug tipe data 
# Temukan keduanya

# MASUKAN
nama_barang = input("Nama barang: ")
harga_satuan = input("Harga satuan: ")
jumlah = input("Jumlah beli: ")

# PROSES
total = harga_satuan * jumlah

# KELUARAN
print(f"{nama_barang} x{jumlah} = Rp{total}")

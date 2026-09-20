# MASUKAN
nama_barang = input("Nama barang: ")
harga = int(input("Harga satuan: "))
jumlah = int(input("Jumlah beli: "))
# PROSES
total = harga * jumlah
# KELUARAN
print(f"{nama_barang} x{jumlah} = Rp{total}")
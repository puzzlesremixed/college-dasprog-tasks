# MASUKAN
nama_barang = input("Nama barang: ") 
harga_satuan = int(input("Harga satuan (Rp): ")) 
jumlah = int(input("Jumlah beli: "))

# PROSES
total = harga_satuan * jumlah

# KELUARAN
rupiah = f"Rp{total:,}".replace(",", ".") 
print(f"{nama_barang} x{jumlah} = {rupiah}")
